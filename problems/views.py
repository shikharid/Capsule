import json
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

from rest_framework import permissions, generics
from problems.models import Assignment
from problems.permission import IsStudent
from problems.serializers import AssignmentSerializer


class PendingAssignmentAPIView(generics.ListAPIView):
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsStudent]

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
    permission_classes = [permissions.IsAuthenticated, IsStudent]

    def get_queryset(self):
        member_id = self.request.user.member_id
        prefix_list = [member_id, ]
        for i in range(1, len(member_id)):
            prefix_list.append(member_id[:-i])
        query_filter = Q(deadline__lt=datetime.now().date()) & Q(batch_prefix__in=prefix_list)
        queryset = Assignment.objects.filter(query_filter)
        return queryset



