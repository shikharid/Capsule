from rest_framework import serializers

from judge.models import Submission
from problems.models import ProblemScore


class SubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submission
        fields = ['id',
                  'problem_id',
                  'user_id',
                  'language',
                  'code']
        read_only_fields = ['verdict', 'spoj_id', 'created_on', 'updated_on']


class SubmissionStatusSerializer(serializers.ModelSerializer):
    problem_name = serializers.CharField(source='problem_id.name', read_only=True)
    points = serializers.CharField(source='problem_id.points', read_only=True)
    member_id = serializers.CharField(source='user_id.member_id', read_only=True)

    def to_representation(self, instance):
        # To add current user score to output
        score = ProblemScore.objects.get(problem=instance.problem_id, student=instance.user_id).score
        resp = super(SubmissionStatusSerializer, self).to_representation(instance)
        resp['score'] = score
        return resp

    class Meta:
        model = Submission
        fields = ['id',
                  'problem_name',
                  'problem_id',
                  'user_id',
                  'member_id',
                  'points',
                  'language',
                  'code',
                  'verdict',
                  'memory_taken',
                  'time_taken',
                  'error_info',
                  'created_on']
        read_only_fields = ['spoj_id', 'created_on', 'updated_on', 'problem_name', 'points', 'member_id']




