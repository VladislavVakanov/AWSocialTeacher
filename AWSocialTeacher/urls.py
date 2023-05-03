from django.contrib import admin
from django.urls import path

from user.views import login

from students.views import students


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', login, name='login'),
    path('students/', students, name='students')
]
