from rest_framework import serializers

from apps.account.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'last_name')
