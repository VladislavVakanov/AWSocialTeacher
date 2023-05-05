from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm

from user.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'login',
        'id': 'username',
        'name': 'username',
        'placeholder': 'Логин',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': 'password',
        'id': 'password',
        'name': 'password',
        'placeholder': 'Пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input'
    }))
    role = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'readonly': True
    }))
    group_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'readonly': True
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'role', 'group_number', 'email')
