from django.shortcuts import render


def students(request):
    return render(request, 'mainpage/students.html')
