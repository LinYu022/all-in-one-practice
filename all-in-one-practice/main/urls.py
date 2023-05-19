from django.contrib import admin
from django.urls import path
from login import login_views
from django.views.generic import RedirectView
from index import index_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='login/')),
    path('login/', login_views.login, name='login'),
    path('myAdmin/', login_views.admin_page, name='admin_page'),
    path('teacher/', login_views.teacher_page, name='teacher_page'),
    path('student/', login_views.student_page, name='student_page'),
    path('index/', index_views.index_page, name='index_page'),
]
