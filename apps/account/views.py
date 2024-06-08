from uuid import uuid4

from django.contrib.auth.models import User
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView

from .serializer import UserSerialize


class Register(APIView):
    """This view will only be used by the client."""

    def post(self, request: Request, format=None):
        request.data['username'] = str(uuid4())

        try:
            User.objects.get(email=request.data['email'])
            return JsonResponse(data={"errors": ["The email is already in use."]},
                                status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            pass

        serializer = UserSerialize(data=request.data)

        if not serializer.is_valid():
            return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()

        return JsonResponse(data={'message': 'Success'}, status=status.HTTP_200_OK)


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
