from datetime import datetime
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import Http404

from rest_framework import generics, serializers
from rest_framework.decorators import detail_route
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from judge.serializers import SubmissionStatusSerializer

from problems.models import Assignment, Problem, ProblemScore
from judge.models import Submission
from review.tasks import plagiarism_check
from authentication.models import User
from problems.permission import IsStudent, IsFaculty, IsOwner
from problems.serializers import AssignmentSerializer, ProblemSerializer
from review.models import PlagiarismRequest, PlagiarismScore, AssignmentReview, ProblemReview


class ListAssignmentAPIView(generics.ListAPIView):
    serializer_class = AssignmentSerializer
    permission_classes = [IsFaculty]

    def get_queryset(self):
        query_filter = Q(deadline__lt=datetime.now().date()) & Q(faculty_id=self.request.user) & Q(review_done=False)
        queryset = Assignment.objects.filter(query_filter)
        return queryset


class ListStudentAPIView(generics.ListAPIView):
    permission_classes = [IsFaculty, IsOwner]
    queryset = Assignment.objects.all()

    def list(self, request, *args, **kwargs):
        assignment_id = self.kwargs.get('assignment_id', None)
        if assignment_id is None:
            return Response({'error': 'No assignment ID found'})

        response = []
        score = {}
        assignment = get_object_or_404(Assignment.objects.all(), id=assignment_id)
        user_queryset = User.objects.filter(member_id__startswith=assignment.batch_prefix)
        user_list = user_queryset.values_list('member_id', flat=True)
        problem_queryset = Problem.objects.filter(assignment_id=assignment)
        problem_list = problem_queryset.values_list('id', flat=True)

        score = {user: {prob: 0 for prob in problem_list} for user in user_list}

        filter_query = Q(problem_id__in=problem_queryset) & Q(user_id__in=user_queryset) & Q(verdict=Submission.AC)
        submission_queryset = Submission.objects.filter(filter_query)

        for submission in submission_queryset:
            user_id = submission.user_id.member_id
            problem_id = submission.problem_id.id
            if score[user_id][problem_id] is 0:
                score[user_id][problem_id] = ProblemScore.objects.get(student=submission.user_id,
                                                                      problem=submission.problem_id).score

        for user in user_list:
            points = 0
            for prob in problem_list:
                points += score[user][prob]
            response.append({'member_id': user, 'points': points})

        return Response(response)


class ReviewAssignmentViewSet(GenericViewSet):
    """
    View Set for review model
    """

    lookup_field = 'assignment_id'
    lookup_value_regex = '[\d]+'
    serializer_class = AssignmentSerializer
    permission_classes = [IsFaculty, IsOwner]

    @detail_route(methods=['post'], url_path='mark-review-done')
    def mark_review_done(self, request, *args, **kwargs):
        assignment_id = self.kwargs.get('assignment_id', None)
        if assignment_id is None:
            raise Http404
        assignment = get_object_or_404(Assignment.objects.all(), id=assignment_id)

        assignment.review_done = True
        assignment.save()
        resp = {'status': 'success', 'message': 'Marked review complete'}
        return Response(resp, status=status.HTTP_204_NO_CONTENT)

    @detail_route(methods=['post'], url_path='plagiarism-request')
    def plagiarism_request(self, request, *args, **kwargs):
        assignment_id = self.kwargs.get('assignment_id', None)
        if assignment_id is None:
            raise Http404
        assignment = get_object_or_404(Assignment.objects.all(), id=assignment_id)
        try:
            PlagiarismRequest.objects.get(assignment=assignment)
            return Response({'status': 'failure', 'message': 'Plagiarism Check Request Already added'},
                            status=status.HTTP_400_BAD_REQUEST)
        except PlagiarismRequest.DoesNotExist:
            instance = PlagiarismRequest(assignment=assignment)
            instance.save()
            return Response({'status': "success", 'message': 'Plagiarism Check Request Added'},
                            status=status.HTTP_201_CREATED)

    @detail_route(methods=['get'], url_path='plagiarism-request-status')
    def plagiarism_request_status(self, request, *args, **kwargs):
        assignment_id = self.kwargs.get('assignment_id', None)
        if assignment_id is None:
            raise Http404
        assignment = get_object_or_404(Assignment.objects.all(), id=assignment_id)
        try:
            instance = PlagiarismRequest.objects.get(assignment=assignment)
            resp = {'status': 'success', 'message': 'Plagiarism check in progress', 'state': False}
            if instance.status:
                resp['message'] = 'Plagiarism check complete'
                resp['state'] = True
            return Response(resp, status=status.HTTP_200_OK)
        except PlagiarismRequest.DoesNotExist:
            resp = {'status': 'failure', 'message': 'No plagiarism check request found'}
            return Response(resp, status=status.HTTP_404_NOT_FOUND)


class ReviewStudentViewSet(GenericViewSet):
    """
    View Set for student review
    """

    lookup_field = 'student_id'
    lookup_value_regex = '[A-Za-z0-9]+'
    serializer_class = AssignmentSerializer
    permission_classes = [IsFaculty, IsOwner]
    queryset = Assignment.objects.all()

    @detail_route(methods=['get'], url_path='code-list')
    def code_list(self, request, *args, **kwargs):
        student_id = kwargs.get('student_id')
        assignment_id = kwargs.get('assignment_id')
        student = get_object_or_404(User.objects.all(), member_id=student_id)
        assignment = get_object_or_404(Assignment.objects.all(), id=assignment_id)
        problem_queryset = Problem.objects.filter(assignment_id=assignment)
        filter_query = Q(problem_id__in=problem_queryset) & Q(user_id=student) & Q(verdict=Submission.AC)
        submission_queryset = Submission.objects.filter(filter_query).order_by('-updated_on')
        submission_latest = []
        submission_found = {problem.id: False for problem in problem_queryset}

        # Reduce submission list to latest submissions
        for submission in submission_queryset:
            if not submission_found[submission.problem_id.id]:
                submission_latest.append(submission)
                submission_found[submission.problem_id.id] = True
        serializer = SubmissionStatusSerializer(submission_latest, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'], url_path='(?P<problem_id>[\d]+)')
    def check_code(self, request, *args, **kwargs):

        student_id = kwargs.get('student_id')
        problem_id = kwargs.get('problem_id')

        student = get_object_or_404(User.objects.all(), member_id=student_id)
        problem = get_object_or_404(Problem.objects.all(), id=problem_id)

        score = PlagiarismScore.objects.get(student_a=student)
        resp = {'ratio': score.score}

        filter_query = Q(problem_id=problem) & Q(user_id=student) & Q(verdict=Submission.AC)
        submission_a = Submission.objects.filter(filter_query).order_by('-updated_on')[:1].get()
        filter_query = Q(problem_id=problem) & Q(user_id=score.student_b) & Q(verdict=Submission.AC)
        submission_b = Submission.objects.filter(filter_query).order_by('-updated_on')[:1].get()

        resp['submission'] = SubmissionStatusSerializer(submission_a).data
        resp['caughtWith'] = SubmissionStatusSerializer(submission_b).data

        return Response(resp)

    @detail_route(methods=['post'], url_path='(?P<problem_id>[\d]+)/reduce')
    def reduce_score(self, request, *args, **kwargs):

        student_id = kwargs.get('student_id')
        problem_id = kwargs.get('problem_id')

        student = get_object_or_404(User.objects.all(), member_id=student_id)
        problem = get_object_or_404(Problem.objects.all(), id=problem_id)
        assignment = problem.assignment_id
        try:
            instance = PlagiarismRequest.objects.get(assignment=assignment)
            if not instance.status:
                return Response({'status': 'failure', 'message': 'Plagiarism Check not done'},
                                status=status.HTTP_400_BAD_REQUEST)
            points = self.request.data.get('points', None)
            print "points", points
            if points is None or not (0 <= points <= problem.points):
                return Response({'status': 'failure', 'message': 'Invalid point allocation'},
                                status=status.HTTP_400_BAD_REQUEST)
            problem_score = get_object_or_404(ProblemScore, student=student, problem=problem)
            problem_score.score = points
            problem_score.save()
            return Response({'status': 'success', 'message': 'Points Updated'},
                            status=status.HTTP_200_OK)
        except PlagiarismRequest.DoesNotExist:
            return Response({'status': 'failure', 'message': 'Plagiarism Check not done'},
                            status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['post'], url_path='mail')
    def assignment_review(self, request, *args, **kwargs):
        review = self.request.data.get('review', None)
        if not review:
            return Response({'status': 'failure'}, status=status.HTTP_400_BAD_REQUEST)

        student_id = kwargs.get('student_id')
        assignment_id = kwargs.get('assignment_id')

        student = get_object_or_404(User.objects.all(), member_id=student_id)
        assignment = get_object_or_404(Assignment.objects.all(), id=assignment_id)
        instance = AssignmentReview(student=student, assignment=assignment, review=review)
        instance.save()
        return Response({'status': 'success', 'message': 'Review added'},
                        status=status.HTTP_201_CREATED)

    @detail_route(methods=['post'], url_path='(?P<problem_id>[\d]+)/mail')
    def submission_review(self, request, *args, **kwargs):
        review = self.request.data.get('review', None)
        if not review:
            return Response({'status': 'failure'}, status=status.HTTP_400_BAD_REQUEST)

        student_id = kwargs.get('student_id')
        problem_id = kwargs.get('problem_id')

        student = get_object_or_404(User.objects.all(), member_id=student_id)
        problem = get_object_or_404(Problem.objects.all(), id=problem_id)
        instance = ProblemReview(student=student, problem=problem, review=review)
        instance.save()
        return Response({'status': 'success', 'message': 'Review added'},
                        status=status.HTTP_201_CREATED)


@receiver(post_save, sender=PlagiarismRequest)
def run_plagiarism(sender, instance, created, **kwargs):
    if created:
        plagiarism_check.delay(instance)


