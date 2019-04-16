from django.db import models
from django.contrib.auth.models import AbstractUser


class Client(AbstractUser):

    phone = models.CharField(max_length=32)
    address = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'client'
