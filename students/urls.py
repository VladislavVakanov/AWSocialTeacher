from django.urls import path

from students.views import (StudentListView, StudentDetailView, AllStudentsFromGroupListView,
                            show_group_report, SocialTeacherListView, PsychologistListView, return_to_previous_page)

app_name = 'students'


urlpatterns = [
    path('curator', StudentListView.as_view(), name='show_curator_page'),
    path('psychologist/', PsychologistListView.as_view(), name='show_psychologist_page'),
    path('social-teacher/', SocialTeacherListView.as_view(), name='show_social_teacher_page'),
    path('group/<int:group>/', AllStudentsFromGroupListView.as_view(), name='show_students_list_page'),
    path(f'group/<int:group>/<str:last_name>/', StudentDetailView, name='show_info_about_student'),
    path('group/reports/<int:group>/', show_group_report, name='show_group_reports'),
]
