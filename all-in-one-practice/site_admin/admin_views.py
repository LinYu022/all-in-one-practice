from django.http import HttpResponse
from database.models import tb_student, tb_teacher
from django.shortcuts import render, redirect


# Create your views here.
def add_student(request):
    if request.method == 'POST':
        sid = request.POST.get('sid')
        name = request.POST.get('stu_name')
        phone = request.POST.get('stu_phone')
        email = request.POST.get('stu_email')
        bjid = request.POST.get('bjid')

    student = tb_student(sid=sid, name=name, phone=phone, email=email, bjid=bjid)
    student.save()
    return HttpResponse("<p>数据添加成功！</p>")


def add_teacher(request):
    if request.method == 'POST':
        tid = request.POST.get('tid')
        tname = request.POST.get('tname')
        tphone = request.POST.get('tphone')
        temail = request.POST.get('temail')

    teacher = tb_teacher(tid=tid, tname=tname, phone=tphone, email=temail)
    teacher.save()
    return HttpResponse("<p>数据添加成功！</p>")


def update_student(request):
    if request.method == 'POST':
        student_id = request.POST['sid']
        student = tb_student.objects.get(sid=student_id)
        student.name = request.POST['name']
        student.phone = request.POST['phone']
        student.email = request.POST['email']
        student.bjid = request.POST['bjid']
        student.save()
        return redirect('student_info')
    else:
        return render(request, 'student_info.html')

# def update_teacher(request):
