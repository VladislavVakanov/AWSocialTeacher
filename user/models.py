from django.db import models

from django.contrib.auth.models import AbstractUser, Group




class User(AbstractUser):
    role = models.CharField(max_length=128)
    group_number = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f'{self.username}({self.last_name} {self.first_name})'
