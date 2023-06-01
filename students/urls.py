from django.urls import path

from students.views import (StudentListView, StudentDetailView, show_psychologist_page, show_social_teacher_page,
                            show_all_students_from_group_page, show_all_students_for_curator)

app_name = 'students'


urlpatterns = [
    path('', StudentListView.as_view(), name='show_students'),
    path('psychologist/', show_psychologist_page, name='show_psychologist_page'),
    path('socialteacher/', show_social_teacher_page, name='show_social_teacher_page'),
    path('student/<str:last_name>/', StudentDetailView.as_view(), name='show_info_about_student'),
    path('student_list/group/<int:group>/', show_all_students_from_group_page, name='show_students_list_page'),
]
