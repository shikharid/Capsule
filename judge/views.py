from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from judge.models import Submission

from judge.serializers import SubmissionSerializer, SubmissionStatusSerializer
from problems.models import Problem, Assignment


class SubmissionView(generics.CreateAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            assignment_obj = Assignment.objects.get(id=self.kwargs.get('assignment_id', None))
            batch_prefix = assignment_obj.batch_prefix

            if not (self.request.user.is_faculty or self.request.user.member_id.startswith(batch_prefix)):
                return Response(status=status.HTTP_400_BAD_REQUEST)

            request.data['user_id'] = self.request.user.id
            request.data['problem_id'] = self.kwargs.get('problem_id', None)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        except Problem.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        except Assignment.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SubmissionStatusAPIView(generics.RetrieveAPIView):
    serializer_class = SubmissionStatusSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Submission.objects.filter(user_id=self.request.user)
