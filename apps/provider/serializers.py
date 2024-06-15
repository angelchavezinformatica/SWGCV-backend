from rest_framework import serializers

from .models import Provider


class ProviderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ProviderSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_length=9)


class ProviderSerializerPATCH(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_length=9)
