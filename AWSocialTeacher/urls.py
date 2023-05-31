from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls, name='admin_page'),
    path('', include('user.urls'), name='user'),
    path('students/', include('students.urls'), name='students'),
]
