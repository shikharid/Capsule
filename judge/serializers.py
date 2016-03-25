from rest_framework import serializers

from judge.models import Submission


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

    class Meta:
        model = Submission
        fields = ['id',
                  'problem_id',
                  'user_id',
                  'language',
                  'code',
                  'verdict',
                  'created_on']
        read_only_fields = ['spoj_id', 'created_on', 'updated_on']




