from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    role = models.CharField(max_length=128)

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' | ' + self.role
