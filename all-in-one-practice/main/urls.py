from django.contrib import admin
from django.urls import path
from login import login_views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='login/')),
    path('admin/', admin.site.urls),
    path('login/', login_views.login, name='login'),
    path('myAdmin/', login_views.admin_page, name='admin_page'),
    path('teacher/', login_views.teacher_page, name='teacher_page'),
    path('student/', login_views.student_page, name='student_page'),
]
