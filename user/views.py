from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from user.forms import UserLoginForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                if user.role == 'admin':
                    return HttpResponseRedirect('admin/')
                else:
                    return HttpResponseRedirect('students/')
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'authorization/login.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'authorization/profile.html', context)
