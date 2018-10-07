from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    kudos = models.IntegerField(default=0)
    bio = models.CharField(max_length=512, blank=True, default='')

    def __str__(self):
        return self.username
