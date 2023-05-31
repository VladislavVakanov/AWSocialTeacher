from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from students.models import Student
from user.models import User


def is_curator(user):
    return user.is_authenticated and user.role == 'Куратор'



@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_curator), name='dispatch')
class StudentListView(ListView):
    model = Student
    template_name = 'mainpage/main_curator_page.html'
    context_object_name = 'students'
    ordering = ['last_name']

    def get_queryset(self):
        return super().get_queryset().filter(group_number=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group'] = self.request.user.group_number
        return context



@method_decorator(login_required, name='dispatch')
class StudentDetailView(DetailView):
    model = Student
    template_name = 'mainpage/student_page.html'
    context_object_name = 'student'

    def get_object(self):
        # curator_index = self.request.user.id
        last_name = self.kwargs['last_name']
        return get_object_or_404(Student, last_name=last_name)

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


@login_required
def show_psychologist_page(request):
    context = {
        'user': request.user.role
    }
    print(request.user.role)
    return render(request, 'mainpage/psychologist.html', context)


@login_required
def show_social_teacher_page(request):
    groups = User.objects.filter(group_number__isnull=False).exclude(group_number='').order_by('group_number')
    context = {
        'user': request.user.role,
        'groups': groups
    }
    return render(request, 'mainpage/social_teacher.html', context)


@login_required
def show_all_students_from_group_page(request, group):
    # groups = User.objects.filter(group_number__isnull=False).exclude(group_number='').order_by('group_number')
    curator_index = User.objects.get(group_number=group)
    students = curator_index.student_set.get_queryset()
    print(students)
    context = {
        'user': request.user.role,
        # 'groups': groups
    }
    return render(request, 'mainpage/students_list_page.html', context)
