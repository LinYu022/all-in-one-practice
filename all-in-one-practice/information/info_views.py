from django.shortcuts import render
from database.models import tb_student, tb_teacher


# Create your views here.


def student_info(request):
    students = tb_student.objects.all()
    return render(request, 'student_info.html', {'students': students})


def teacher_info(request):
    teachers = tb_teacher.objects.all()
    return render(request, 'teacher_info.html', {'teachers': teachers})
