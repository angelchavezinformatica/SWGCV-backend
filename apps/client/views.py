from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
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
