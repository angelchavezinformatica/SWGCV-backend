from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    confirm = models.BooleanField(null=True, blank=True)
    token = models.CharField(null=True, blank=True, max_length=40)

    def __str__(self):
        return self.username
