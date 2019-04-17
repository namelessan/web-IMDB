from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username