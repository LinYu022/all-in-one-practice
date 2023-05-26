from django.http import HttpResponse
from django.shortcuts import render
from database.models import tb_student
from database.models import tb_teacher


# Create your views here.
def register(request):
    return render(request, 'register.html')


def stu_register(request):
    if request.method == 'POST':
        sid = request.POST.get('sid')
        stu_password = request.POST.get('stu_password')
        stu_name = request.POST.get('stu_name')
        stu_phone = request.POST.get('stu_phone')
        stu_email = request.POST.get('stu_email')
        bjid = request.POST.get('bjid')

    student = tb_student(sid=sid, password=stu_password, name=stu_name, phone=stu_phone, email=stu_email, bjid=bjid)
    student.save()
    return HttpResponse("<p>学生注册成功！</p>")


def t_register(request):
    if request.method == 'POST':
        tid = request.POST.get('tid')
        tpassword = request.POST.get('tpassword')
        tname = request.POST.get('tname')
        tphone = request.POST.get('tphone')
        temail = request.POST.get('temail')

    teacher = tb_teacher(tid=tid, password=tpassword, tname=tname, phone=tphone, email=temail)
    teacher.save()
    return HttpResponse("<p>教师注册成功！</p>")
