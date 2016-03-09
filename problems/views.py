from datetime import datetime
from django.db.models import Q

from rest_framework import generics, serializers
from rest_framework.response import Response

from problems.models import Assignment, Problem, TestCase
from problems.permission import IsStudent, IsFaculty
from problems.serializers import AssignmentSerializer, ProblemSerializer, EditAssignmentSerializer, \
    EditProblemSerializer, TestCaseSerializer, EditTestCaseSerializer


class PendingAssignmentAPIView(generics.ListAPIView):
    serializer_class = AssignmentSerializer
    permission_classes = [IsStudent]

    def get_queryset(self):
        member_id = self.request.user.member_id
        prefix_list = [member_id, ]
        for i in range(1, len(member_id)):
            prefix_list.append(member_id[:-i])
        query_filter = Q(deadline__gte=datetime.now().date()) & Q(batch_prefix__in=prefix_list)
        queryset = Assignment.objects.filter(query_filter)
        return queryset


class CompletedAssignmentAPIView(generics.ListAPIView):
    serializer_class = AssignmentSerializer
    permission_classes = [IsStudent]

    def get_queryset(self):
        member_id = self.request.user.member_id
        prefix_list = [member_id, ]
        for i in range(1, len(member_id)):
            prefix_list.append(member_id[:-i])
        query_filter = Q(deadline__lt=datetime.now().date()) & Q(batch_prefix__in=prefix_list)
        queryset = Assignment.objects.filter(query_filter)
        return queryset


class ProblemListAPIView(generics.ListAPIView):
    permission_classes = [IsStudent]
    serializer_class = ProblemSerializer

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return Response({'error': 'Cannot GET on problem-list'})

    def get_queryset(self):
        try:
            assignment_id = self.request.data.get('assignment_id', None)
            assignment_obj = Assignment.objects.get(id=assignment_id)
            return Problem.objects.all().filter(assignment_id=assignment_obj)
        except Exception:
            return Problem.objects.none()


# Faculty End Views

class AddAssignment(generics.CreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsFaculty]


class ListAssignment(generics.ListAPIView):
    serializer_class = AssignmentSerializer
    permission_classes = [IsFaculty]

    def get_queryset(self):
        return Assignment.objects.filter(faculty_id=self.request.user)


class EditAssignment(generics.RetrieveUpdateAPIView):

    serializer_class = EditAssignmentSerializer
    permission_classes = [IsFaculty]

    def get_queryset(self):
        return Assignment.objects.filter(faculty_id=self.request.user)


class ListProblems(generics.ListAPIView):
    serializer_class = ProblemSerializer
    permission_classes = [IsFaculty]

    def get_queryset(self):
        assignment_id = self.kwargs.get('assignment_id', None)
        try:
            assignment_obj = Assignment.objects.get(id=assignment_id, faculty_id=self.request.user)
            return Problem.objects.filter(assignment_id=assignment_obj)
        except Assignment.DoesNotExist:
            return Problem.objects.none()


class AddProblems(generics.CreateAPIView):
    serializer_class = ProblemSerializer
    permission_classes = [IsFaculty]

    def create(self, request, *args, **kwargs):
        request.data['assignment_id'] = self.kwargs.get('assignment_id', None)

        try:
            Assignment.objects.get(id=request.data['assignment_id'], faculty_id=self.request.user)
        except Assignment.DoesNotExist:
            request.data['assignment_id'] = None

        return super(AddProblems, self).create(request, *args, **kwargs)


class EditProblems(generics.RetrieveUpdateAPIView):

    queryset = Problem.objects.all()
    serializer_class = EditProblemSerializer
    permission_classes = [IsFaculty]

    def get_object(self):
        assignment_id = self.kwargs.get('assignment_id', None)
        problem_id = self.kwargs.get('problem_id', None)

        try:
            assignment_obj = Assignment.objects.get(id=assignment_id, faculty_id=self.request.user)
            return Problem.objects.get(id=problem_id, assignment_id=assignment_obj)

        except Problem.DoesNotExist:
            raise serializers.ValidationError('Error.No such Problem exists.')


class AddTestCase(generics.CreateAPIView):
    """
    Add's test case after verifying problem and assignment id
    Faculty can only add if the assignment id belongs to them
    """
    serializer_class = TestCaseSerializer
    permission_classes = [IsFaculty]

    def create(self, request, *args, **kwargs):
        request.data['problem_id'] = self.kwargs.get('problem_id', None)

        try:
            Assignment.objects.get(id=self.kwargs.get('assignment_id', None), faculty_id=self.request.user)
        except Assignment.DoesNotExist:
            request.data['problem_id'] = None

        return super(AddTestCase, self).create(request, *args, **kwargs)


class EditTestCase(generics.ListAPIView):
    """
    Toggle use/don't use a test case when judging a batch of submissions.
    Useful when same assignment has to be implemented using multiple algo's.
    """
    serializer_class = EditTestCaseSerializer
    permission_classes = [IsFaculty]

    def get_queryset(self):
        assignment_id = self.kwargs.get('assignment_id', None)
        problem_id = self.kwargs.get('problem_id', None)
        try:
            Assignment.objects.get(id=assignment_id, faculty_id=self.request.user)
            problem_obj = Problem.objects.get(id=problem_id)
            return TestCase.objects.filter(problem_id=problem_obj)
        except Assignment.DoesNotExist:
            return TestCase.objects.none()
        except Problem.DoesNotExist:
            return TestCase.objects.none()


class RemoveTestCase(generics.DestroyAPIView):

    """
    Verifies assignment id and problem id before deleting the testcase
    The testcase is removed from TestCase database table
    """
    # TODO - Remove test case from folder also
    serializer_class = EditTestCaseSerializer
    permission_classes = [IsFaculty]

    def get_object(self):
        assignment_id = self.kwargs.get('assignment_id', None)
        problem_id = self.kwargs.get('problem_id', None)
        testcase_id = self.kwargs.get('id', None)
        try:
            Assignment.objects.get(id=assignment_id, faculty_id=self.request.user)
            problem_obj = Problem.objects.get(id=problem_id)
            testcase_obj = TestCase.objects.get(id=testcase_id, problem_id=problem_obj)
            return testcase_obj
        except Assignment.DoesNotExist:
            return TestCase.objects.none()
        except Problem.DoesNotExist:
            return TestCase.objects.none()
        except TestCase.DoesNotExist:
            return TestCase.objects.none()

















