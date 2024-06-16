from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from .models import User
from .serializer import RegisterSerialize


class Register(APIView):
    """This view will only be used by the client."""

    def post(self, request: Request, format=None):
        user = RegisterSerialize(data=request.data)

        if not user.is_valid():
            return Response(data=user.errors, status=status.HTTP_400_BAD_REQUEST)
        user.save()
        return Response(status=status.HTTP_200_OK)


class Confirm(APIView):
    def get(self, request: Request, token: str, format=None):
        try:
            user = User.objects.get(token=token)
            user.confirm = True
            user.token = None
            user.save()
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)


class Login(APIView):
    """For login:
    - The client must send their email and password.
    - The administrator must send their username and password.
    """

    def post(self, request: Request, format=None):
        username = request.data.get('username')
        email = request.data.get('username', '')
        password = request.data.get('password', '')

        try:
            if username is not None:
                user = User.objects.get(username=username)
            else:
                user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse(data={}, status=status.HTTP_400_BAD_REQUEST)

        if not user.is_superuser or not user.check_password(password):
            return JsonResponse(data={}, status=status.HTTP_400_BAD_REQUEST)

        token = Token.objects.get_or_create(user=user)[0]

        return JsonResponse(data={'token': token.key})


class Auth(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, format=None):
        return JsonResponse(data={'message': 'success'})
