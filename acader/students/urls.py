from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path('register/', views.register, name='register'),
    path('studentregister/', views.studentregister, name='studentregister'),
    path('course/', views.course, name='course'),
    path('marks/', views.marks, name='marks'),
    path('term/', views.terms, name='term'),
    path('faculty/', views.facultys, name='facultys'),
    path('grade/', views.grades, name='grades'),
    path('teacherlogin/', views.teacherlogin, name='teacherlogin'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('student-func/', views.student_func, name='student-func'),
    path('teacher-func/', views.teacher_func, name='teacher-func'),
    path('do_logout/', views.do_logout, name='do_logout'),
    path('do_logout/', views.do_logout, name='do_logout'),
]