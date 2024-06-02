from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'password', 'first_name', 'last_name']
