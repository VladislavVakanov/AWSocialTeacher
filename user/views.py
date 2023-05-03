from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from user.models import User
from user.forms import UserLoginForm

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
                    return HttpResponseRedirect(reverse('students'))

    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'authorization/login.html', context)
