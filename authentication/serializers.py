from rest_framework import serializers

from authentication.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'member_id', 'email']
        read_only_fields = ['created_on', 'updated_on']



