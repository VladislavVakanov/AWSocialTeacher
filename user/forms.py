from django import forms
from django.contrib.auth.forms import AuthenticationForm

from user.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'username',
        'name': 'username',
        'placeholder': 'Логин',
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password',
        'id': 'password',
        'name': 'password',
        'placeholder': 'Пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')
