from django.urls import path, include
from students.forms import EmailValidationOnForgotPassword
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path('teacherregister/', views.teacherregister, name='teacherregister'),
    path('studentregister/', views.studentregister, name='studentregister'),
    path('course/', views.course, name='course'),
    path('marks/', views.marks, name='marks'),
    path('term/', views.terms, name='term'),
    path('faculty/', views.facultys, name='facultys'),
    path('grade/', views.grades, name='grades'),
    path('student-func/', views.student_func, name='student-func'),
    path('teacher-func/', views.teacher_func, name='teacher-func'),
    path('do_logout/', views.do_logout, name='do_logout'),
    path('studentcourse/', views.studentcourse, name='studentcourse'),
    path('student_list/', views.student_list, name='student_list'),
    path('student_displaymarks/<int:student_id>', views.student_displaymarks, name='student_displaymarks'),
    path('teacher_list/', views.teacher_list, name='teacher_list'),
    path('search_student/', views.search_student, name='search_student'),
    path('search_teacher/', views.search_teacher, name='search_teacher'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(form_class=EmailValidationOnForgotPassword,template_name='students/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='students/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='students/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='students/password_reset_complete.html'),
         name='password_reset_complete'),
    path('edit_teacher/<str:teacher_id_slug>/', views.edit_teacher, name='edit_teacher'),
    path('edit_student/<str:student_id_slug>/', views.edit_student, name='edit_student'),
    path('delete_teacher/<str:teacher_del_slug>/', views.delete_teacher, name='delete_teacher'),
    path('delete_student/<str:student_del_slug>/', views.delete_student, name='delete_student'),

]