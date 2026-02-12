"""
URL configuration for mainproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import show_student_list, add_student, student_mark, subject, delete_stu, department, delete_per_stu, deleted_stu_list, recover_stu
from main.views import get_student_marks
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_student_list, name="show_student_list"),
    path('add_student/', add_student, name="add_student"),
    path('student_mark/', student_mark, name="student_mark"),
    path('subject/', subject, name="subject"),
    path('department/', department, name="department"),
    path('delete_stu/<id>/', delete_stu, name='delete_stu'),
    path("deleted_stu_list/",deleted_stu_list, name="deleted_stu_list"),
    path("deleted_stu_list/recover_stu/<id>/",recover_stu, name="recover_stu"),
    path('deleted_stu_list/delete_per_stu/<id>/', delete_per_stu, name='delete_per_stu'),
    path("student_marks/<id>/", get_student_marks, name="get_student_marks"),
]
