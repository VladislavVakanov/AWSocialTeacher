from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path


from students.views import students


app_name = 'students'

urlpatterns = [
    path('students/', students, name='students')
]
