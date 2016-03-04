from rest_framework import serializers

from problems.models import Assignment, Problem


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['faculty_id',
                  'name',
                  'batch_prefix',
                  'deadline',
                  'subject_code']
        read_only_fields = ['created_on', 'updated_on']


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['id',
                  'assignment_id',
                  'name',
                  'points', ]
        read_only_fields = ['created_on', 'updated_on']



