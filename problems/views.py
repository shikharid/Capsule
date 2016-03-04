import json
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

from rest_framework import permissions, generics, views
from rest_framework.response import Response
from problems.models import Assignment, Problem
from problems.permission import IsStudent
from problems.serializers import AssignmentSerializer, ProblemSerializer


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










