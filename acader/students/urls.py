from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('studentregister/', views.studentregister, name='studentregister'),
    path('course/', views.course, name='course'),
    path('marks/', views.marks, name='marks'),
    path('term/', views.terms, name='term'),
    path('faculty/', views.facultys, name='facultys'),
    path('grade/', views.grades, name='grades'),
    path('teacherlogin/', views.teacherlogin, name='teacherlogin'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('student-func/', views.base, name='student-func'),
    path('teacher-func/', views.base1, name='teacher-func'),
]