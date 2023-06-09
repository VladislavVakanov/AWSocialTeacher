from django import forms
from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from user.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'role', 'group_number')}),
        ('Личная информация', {'fields': ('last_name', 'first_name', 'email')}),
        ('Разрешения', {'fields': ( 'is_superuser', 'is_staff')}),
        ('Даты', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.unregister(Group)