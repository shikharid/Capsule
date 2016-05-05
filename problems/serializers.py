from datetime import datetime

from rest_framework import serializers

from problems.models import Assignment, Problem, TestCase


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id',
                  'faculty_id',
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
                  'statement',
                  'time_limit',
                  'points', ]
        read_only_fields = ['created_on', 'updated_on']

# Faculty End serializers


class EditAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['name',
                  'batch_prefix',
                  'deadline',
                  'subject_code']
        read_only_fields = ['id', 'faculty_id', 'created_on', 'updated_on']

    def validate_deadline(self, deadline):

        if deadline < datetime.now().date():
            raise serializers.ValidationError('Date cannot be in the past')

        return deadline


class EditProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['name',
                  'statement',
                  'time_limit',
                  'points', ]
        read_only_fields = ['id', 'assignment_id', 'created_on', 'updated_on']


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = ['id',
                  'problem_id',
                  'input',
                  'output',
                  'is_used']
        read_only_fields = ['created_on', 'updated_on']


class EditTestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = ['id',
                  'input',
                  'output',
                  'is_used']
        read_only_fields = ['id', 'problem_id', 'created_on', 'updated_on']





