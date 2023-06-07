from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    ROLE = [
        ('admin', 'admin'),
        ('Куратор', 'Куратор'),
        ('Социальный педагог', 'Социальный педагог'),
        ('Педагог-психолог', 'Педагог-психолог')
    ]
    image = models.ImageField(upload_to='profile_images', blank=True, default='static/files/no-photo.png')
    role = models.CharField(max_length=128, choices=ROLE, blank=False)
    group_number = models.OneToOneField(
        'students.Group', db_column='group_number', db_constraint=False,
        on_delete=models.SET_NULL, null=True, blank=True, to_field='group_number', unique=True
    )

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = f"работника колледжа"
        verbose_name_plural = "Работники колледжа"
