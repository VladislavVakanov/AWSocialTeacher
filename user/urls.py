from django.urls import path

from user.views import ProfileView, CustomLoginView
from user.views import Logout

app_name = 'user'

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', ProfileView.profile, name='profile')
]
