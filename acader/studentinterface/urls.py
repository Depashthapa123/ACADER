from django.urls import path, include
from . import views

urlpatterns = [
    path('course_content/', views.course_content, name='course_content'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student_marks/', views.student_marks, name='student_marks'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('do_logout2/', views.do_logout2, name='do_logout2'),
]