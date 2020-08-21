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
    path('studentcourse/', views.studentcourse, name='studentcourse'),
    path('student_list/', views.student_list, name='student_list'),
    path('student_displaymarks/<int:student_id>', views.student_displaymarks, name='student_displaymarks'),
    path('teacher_list/', views.teacher_list, name='teacher_list'),
    path('search_student/', views.search_student, name='search_student'),
    path('search_teacher/', views.search_teacher, name='search_teacher')

]