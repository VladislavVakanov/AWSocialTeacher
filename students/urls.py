from django.urls import path

from students.views import show_all_students_for_curator, get_info_about_student

app_name = 'students'


urlpatterns = [
    path('', show_all_students_for_curator, name='show_students'),
    path('student/<str:last_name>/', get_info_about_student, name='show_info_about_student'),
]
