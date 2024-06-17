from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from apps.account.models import User
from .serializers import UserModelSerializer


class ClientView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request: Request, format=None):
        q = User.objects.filter(is_superuser=False)
        users = UserModelSerializer(q, many=True)
        return Response(data=users.data)


class ProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, format=None):
        user = UserModelSerializer(request.user)
        return Response(data=user.data, status=status.HTTP_200_OK)
