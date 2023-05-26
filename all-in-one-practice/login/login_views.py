# Create your views here.
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'nenu' and password == 'nenu':
            return redirect('admin_page')
        elif username == '123' and password == '123':
            return redirect('teacher_page')
        else:
            return redirect('student_page')
    return render(request, 'login.html')


def admin_page(request):
    return render(request, 'site_admin.html')


def student_page(request):
    return render(request, 'student.html')


def teacher_page(request):
    return render(request, 'teacher.html')

