from django.contrib import admin
from django.urls import path
from register import register_views
from login import login_views
from site_admin import admin_views
from django.views.generic import RedirectView
from index import index_views

urlpatterns = [
    # path('admin/', site_admin.site.urls),
    path('', RedirectView.as_view(url='login/')),
    path('register/', register_views.register, name='register_page'),
    path('stu_register/', register_views.stu_register, name='stu_register'),
    path('t_register/', register_views.t_register, name='t_register'),
    path('login/', login_views.login, name='login'),
    path('myAdmin/', login_views.admin_page, name='admin_page'),
    path('add_student/', admin_views.add_student, name='add_student'),
    path('add_teacher/', admin_views.add_teacher, name='add_teacher'),
    path('teacher/', login_views.teacher_page, name='teacher_page'),
    path('student/', login_views.student_page, name='student_page'),
    path('index/', index_views.index_page, name='index_page'),
]
