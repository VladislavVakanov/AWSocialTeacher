from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from students.forms import StudentForm
from students.models import Student, Group
from user.models import User


def is_curator(user):
    return user.is_authenticated and user.role == 'Куратор'

def is_social_teacher(user):
    return user.is_authenticated and user.role == 'Социальный педагог'

def is_psychologist(user):
    return user.is_authenticated and user.role == 'Педагог-психолог'


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_curator), name='dispatch')
class StudentListView(ListView):
    model = Student
    template_name = 'pages/main_curator_page.html'
    context_object_name = 'students'
    ordering = ['last_name']

    def get_queryset(self):
        print(self.request.user.groups.all()[0])
        return super().get_queryset().filter(group_number=self.request.user.group_number)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group'] = self.request.user.group_number
        return context


def StudentDetailView(request, last_name):
    student = Student.objects.get(last_name=last_name)
    if request.method == 'POST':
        form = StudentForm(instance=student, data=request.POST, files=request.FILES)
        if form.is_valid():
            if bool(request.FILES) == True:
                if student.image:
                    student.image.delete()
            form.save()
        else:
            print(form.errors)
    else:
        form = StudentForm(instance=student)
    context = {
        'form': form,
        'student': student
    }
    return render(request, 'pages/student_page.html', context)

# @method_decorator(login_required, name='dispatch')
# class StudentDetailView(DetailView):
#     model = Student
#     template_name = 'pages/student_page.html'
#     context_object_name = 'student'
#     form_class = StudentForm
#
#     def get_object(self):
#         # curator_index = self.request.user.id
#         last_name = self.kwargs['last_name']
#         return get_object_or_404(Student, last_name=last_name)


@login_required
def show_all_students_for_curator(request):
    students = Student.objects.filter(group_number=request.user.group_number)
    context = {
        'group': request.user.group_number,
        'students': students
    }
    return render(request, 'pages/main_curator_page.html', context)


@login_required
def get_info_about_student(request, last_name: str):
    curator_index = User.objects.get(id=request.user.id)
    student = curator_index.student_set.get(last_name=last_name)
    context = {
        'student': student
    }
    return render(request, 'pages/student_page.html', context)


@login_required
def show_psychologist_page(request):
    context = {
        'user': request.user.role
    }
    print(request.user.role)
    return render(request, 'pages/psychologist.html', context)


# @login_required
# def show_social_teacher_page(request):
#     groups = User.objects.filter(group_number__isnull=False).exclude(group_number='').order_by('group_number')
#     print(request.user.groups.all())
#     context = {
#         'user': request.user.role,
#         'groups': groups
#     }
#     return render(request, 'pages/social_teacher.html', context)

@login_required
def show_social_teacher_page(request):
    groups = Group.objects.order_by('group_number')
    context = {
        'groups': groups
    }
    return render(request, 'pages/social_teacher.html', context)


@login_required
def show_all_students_from_group_page(request, group):
    students = Student.objects.filter(group_number=group).order_by('last_name')
    context = {
        'group': group,
        'students': students
    }
    return render(request, 'pages/students_list_page.html', context)
