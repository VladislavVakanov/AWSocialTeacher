from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from datetime import date
from students.forms import (StudentForm, AntisocialBehaviorForm, IncentivesForm,
                            IndividualWorkForm, WorkWithParentsForm, SpecialistRecomendationsForm)
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


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_social_teacher), name='dispatch')
class SocialTeacherListView(ListView):
    model = Group
    template_name = 'pages/social_teacher.html'
    context_object_name = 'groups'
    ordering = 'group_number'


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_psychologist), name='dispatch')
class PsychologistListView(ListView):
    model = Group
    template_name = 'pages/psychologist.html'
    context_object_name = 'groups'
    ordering = 'group_number'


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


def StudentDetailView(request, last_name, group):
    if request.method == 'POST':
        if 'form1-submit' in request.POST:
            form1 = StudentForm(instance=get_object_or_404(Student, last_name=last_name), data=request.POST, files=request.FILES)
            if form1.is_valid():
                student = get_object_or_404(Student, last_name=last_name)
                if bool(request.FILES) and student.image:
                    student.image.delete()
                form1.save()
        elif 'form2-submit' in request.POST:
            form2 = IncentivesForm(request.POST)
            if form2.is_valid():
                student = get_object_or_404(Student, last_name=last_name)
                incentives_instance = form2.save(commit=False)
                incentives_instance.save()
                student.incentives.add(incentives_instance)
        elif 'form3-submit' in request.POST:
            form3 = AntisocialBehaviorForm(request.POST)
            if form3.is_valid():
                student = get_object_or_404(Student, last_name=last_name)
                antisocial_instance = form3.save(commit=False)
                antisocial_instance.save()
                student.antisocial_behavior.add(antisocial_instance)
            else:
                print(form3.errors)
        elif 'form4-submit' in request.POST:
            form4 = SpecialistRecomendationsForm(request.POST)
            if form4.is_valid():
                student = get_object_or_404(Student, last_name=last_name)
                specialist_recommendations_instance = form4.save(commit=False)
                specialist_recommendations_instance.save()
                student.specialist_recommendations.add(specialist_recommendations_instance)
        elif 'form5-submit' in request.POST:
            form5 = IndividualWorkForm(request.POST)
            if form5.is_valid():
                student = get_object_or_404(Student, last_name=last_name)
                individualwork_instance = form5.save(commit=False)
                individualwork_instance.save()
                student.individualwork.add(individualwork_instance)
        elif 'form6-submit' in request.POST:
            form6 = WorkWithParentsForm(request.POST)
            if form6.is_valid():
                student = get_object_or_404(Student, last_name=last_name)
                workwithparents_instance = form6.save(commit=False)
                workwithparents_instance.save()
                student.workwithparents.add(workwithparents_instance)
    else:
        form = StudentForm(instance=get_object_or_404(Student, last_name=last_name))
        antisocialbehaviorform = AntisocialBehaviorForm()
        incentivesform = IncentivesForm()
        specialistrecomendationform = SpecialistRecomendationsForm()
        individualworkform = IndividualWorkForm()
        workwithparentsform = WorkWithParentsForm()

    context = {
        'form': StudentForm(instance=get_object_or_404(Student, last_name=last_name)),
        'antisocialbehaviorform': AntisocialBehaviorForm(),
        'incentivesform': IncentivesForm(),
        'specialistrecomendationform': SpecialistRecomendationsForm(),
        'individualworkform': IndividualWorkForm(),
        'workwithparentsform': WorkWithParentsForm(),
        'student': get_object_or_404(Student, last_name=last_name),
        'incentives': get_object_or_404(Student, last_name=last_name).incentives.all(),
        'antisocialbehaviors': get_object_or_404(Student, last_name=last_name).antisocial_behavior.all(),
        'specialistrecommendations': get_object_or_404(Student, last_name=last_name).specialist_recommendations.all(),
        'individualworks': get_object_or_404(Student, last_name=last_name).individualwork.all(),
        'workwithparents': get_object_or_404(Student, last_name=last_name).workwithparents.all(),
        'group': get_object_or_404(Student, last_name=last_name).group_number
    }
    return render(request, 'pages/student_page.html', context)



class AllStudentsFromGroupListView(ListView):
    template_name = 'pages/students_list_page.html'
    context_object_name = 'students'

    def get_queryset(self):
        group = self.kwargs['group']
        return Student.objects.filter(group_number=group).order_by('last_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group = self.kwargs['group']
        context['group'] = group
        return context

@login_required
def show_group_report(request, group):
    context = {
        'group': group,
        'date': {
            'day': str(date.today().day).zfill(2),
            'month': str(date.today().month).zfill(2),
            'year': date.today().year
        }
    }
    return render(request, 'pages/group_report_page.html', context)

