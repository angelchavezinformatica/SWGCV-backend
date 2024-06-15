from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from .models import Provider
from .serializers import (
    ProviderModelSerializer,
    ProviderSerializer,
    ProviderSerializerPATCH,
)


class ProviderView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request: Request, format=None):
        providers = ProviderModelSerializer(Provider.objects.all(), many=True)
        return Response(data=providers.data, status=status.HTTP_200_OK)

    def post(self, request: Request, format=None):
        serializer = ProviderSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        provider = Provider(
            name=serializer.data.get('name'),
            phone_number=serializer.data.get('phone_number'),
        )
        provider.save()

        return Response(status=status.HTTP_200_OK)

    def patch(self, request: Request, format=None):
        serializer = ProviderSerializerPATCH(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            provider = Provider.objects.get(id=serializer.data.get('id'))
        except Provider.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        provider.name = serializer.data.get('name')
        provider.phone_number = serializer.data.get('phone_number')
        provider.save()

        return Response(status=status.HTTP_200_OK)
