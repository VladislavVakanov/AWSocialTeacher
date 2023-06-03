from django.contrib.auth.models import AbstractUser
from django.db import models

from students.models import Group


class User(AbstractUser):
    ROLE = [
        ('admin', 'admin'),
        ('Куратор', 'Куратор'),
        ('Социальный педагог', 'Социальный педагог'),
        ('Педагог-психолог', 'Педагог-психолог')
    ]
    image = models.ImageField(upload_to='profile_images', blank=True)
    role = models.CharField(max_length=128, choices=ROLE)
    group_number = models.OneToOneField(
        Group, db_column='group_number', db_constraint=False,
        on_delete=models.SET_NULL, null=True, blank=True, to_field='group_number', unique=True
    )

    def __str__(self):
        return f'{self.username}({self.last_name} {self.first_name})'
