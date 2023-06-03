from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView

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
            return reverse_lazy('students:show_students')
        elif user.role == 'Социальный педагог':
            return reverse_lazy('students:show_social_teacher_page')
        elif user.role == 'Педагог-психолог':
            return reverse_lazy('students:show_psychologist_page')


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
        context = {
            'form': form
        }
        return render(request, 'pages/profile_page.html', context)


# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 if user.role == 'admin':
#                     return HttpResponseRedirect('admin/')
#                 elif user.role == 'Куратор':
#                     return HttpResponseRedirect(reverse('students:show_students'))
#                 elif user.role == 'Социальный педагог':
#                     return HttpResponseRedirect(reverse('students:show_social_teacher_page'))
#                 elif user.role == 'Педагог-психолог':
#                     return HttpResponseRedirect(reverse('students:show_psychologist_page'))
#     else:
#         form = UserLoginForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'pages/login.html', context)
