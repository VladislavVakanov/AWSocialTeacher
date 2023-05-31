from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from user.forms import UserLoginForm, UserProfileForm


class CustomLoginView(LoginView):
    template_name = 'authorization/login.html'
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
#     return render(request, 'authorization/login.html', context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'form': form,
        'role': request.user.role,
        'group': request.user.group_number,
    }
    return render(request, 'authorization/profile_page.html', context)
