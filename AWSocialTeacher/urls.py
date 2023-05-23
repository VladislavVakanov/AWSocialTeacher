from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from user.views import login




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls'), name='user'),
    path('students/', include('students.urls'), name='students'),
]
