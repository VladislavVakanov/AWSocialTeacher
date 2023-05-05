from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from user.views import login

from students.views import students


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls'), name='user'),
    path('students/', students, name='students'),
]
