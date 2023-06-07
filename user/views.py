from django.contrib import messages
from django.contrib.auth.views import LogoutView, LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from students.models import Student
from user.forms import UserLoginForm, UserProfileForm
from user.models import User


class CustomLoginView(LoginView):
    template_name = 'pages/login.html'
    redirect_authenticated_user = True
    form_class = UserLoginForm
    def get_success_url(self):
        user = self.request.user
        if user.role == 'admin':
            return reverse_lazy('admin:index')
        elif user.role == 'Куратор':
            return reverse_lazy('students:show_curator_page')
        elif user.role == 'Социальный педагог':
            return reverse_lazy('students:show_social_teacher_page')
        elif user.role == 'Педагог-психолог':
            return reverse_lazy('students:show_psychologist_page')

    def form_invalid(self, form):
        messages.error(self.request, 'Неверные данные')
        return super().form_invalid(form)


class Logout(LogoutView):
    next_page = reverse_lazy('user:login')


class ProfileView():
    def profile(request):
        if request.method == 'POST':
            form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
            if form.is_valid():
                user_profile = User.objects.get(id=request.user.id)
                if bool(request.FILES) == True:
                    if user_profile.image:
                        user_profile.image.delete()
                form.save()
                return HttpResponseRedirect(reverse_lazy('user:profile'))
        else:
            form = UserProfileForm(instance=request.user)
        if request.user.role == 'Куратор':
            students = Student.objects.filter(group_number=request.user.group_number)
            histories = []
            for student in students:
                non_empty_histories = student.history.filter(history_date__isnull=False).exclude(last_name='').order_by('history_date')
                histories.extend(non_empty_histories)
        else:
            students = Student.objects.all()
            histories = []
            for student in students:
                non_empty_histories = student.history.filter(history_date__isnull=False).exclude(last_name='').order_by('history_date')
                histories.extend(non_empty_histories)
        sorted_histories = sorted(histories, key=lambda x: x.history_date)

        context = {
            'form': form,
            'histories': reversed(sorted_histories),

        }
        return render(request, 'pages/profile_page.html', context)
