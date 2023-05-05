from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def students(request):
    return render(request, 'mainpage/students.html')
