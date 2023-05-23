from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from user.models import User


@login_required
def show_all_students_for_curator(request):
    curator_index = User.objects.get(id=request.user.id)
    students = curator_index.student_set.order_by('last_name')
    context = {
        'group': request.user.group_number,
        'students': students
    }
    return render(request, 'mainpage/main_curator_page.html', context)


@login_required
def get_info_about_student(request, last_name: str):
    curator_index = User.objects.get(id=request.user.id)
    student = curator_index.student_set.get(last_name=last_name)
    context = {
        'student': student
    }
    return render(request, 'mainpage/student_page.html', context)
