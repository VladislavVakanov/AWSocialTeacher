from django.urls import path

from user.views import login, profile


app_name = 'user'

urlpatterns = [
    path('', login, name='login'),
    path('profile/', profile, name='profile')
]
