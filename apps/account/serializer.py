import uuid
import re

from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework import serializers

from .models import User


class RegisterSerialize(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=256)
    phone_number = serializers.CharField(max_length=15)

    def create(self, validated_data):
        user = User(
            username=str(uuid.uuid4()),
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
        )
        token = default_token_generator.make_token(user)
        user.set_password(validated_data['password'])
        user.confirm = False
        user.token = token

        full_link = f'{settings.CLIENT_SERVER}auth/confirm_account/{token}'

        send_mail(
            subject='Confirma tu dirección de correo',
            message=f'Confirmar cuenta: {full_link}',
            html_message=f'''<p>Haz <a href="{full_link}">click</a> para confirmar tu cuenta</p>''',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False
        )
        user.save()
        return user

    def validate_email(self, value):
        try:
            User.objects.get(email=value)
            raise serializers.ValidationError("The email is already in use.")
        except User.DoesNotExist:
            pass
        return value

    def validate_password(self, value):
        # Minimum length of 12 characters
        if len(value) < 12:
            raise serializers.ValidationError(
                "Password must be at least 12 characters long.")

        # Maximun length of 256 characters
        if len(value) > 256:
            raise serializers.ValidationError(
                "Password must be at least 256 characters long.")

        # Must include at least one uppercase letter
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError(
                "Password must include at least one uppercase letter.")

        # Must include at least one lowercase letter
        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError(
                "Password must include at least one lowercase letter.")

        # Must include at least one digit
        if not re.search(r'\d', value):
            raise serializers.ValidationError(
                "Password must include at least one digit.")

        # Must include at least one special character
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise serializers.ValidationError(
                "Password must include at least one special character.")

        return value
