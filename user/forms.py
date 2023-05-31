from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.core.validators import EmailValidator

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
    }), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input'
    }), required=False)
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input'
    }), required=False, validators=[EmailValidator(message='Некорректный адрес электронной почты')])
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input'
    }), required=False)
    role = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'readonly': 'readonly'
    }), required=False)
    group_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'readonly': 'readonly'
    }), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'role', 'group_number')
