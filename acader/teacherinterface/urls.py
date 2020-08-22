from django.urls import path, include
from . import views

urlpatterns = [
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher_marks/', views.teacher_marks, name='teacher_marks'),
    path('teacher_profile/', views.teacher_profile, name='teacher_profile'),
    path('do_logout1/', views.do_logout1, name='do_logout1'),
    path('teacher_displaymarks/<int:student_id>', views.teacher_displaymarks, name='teacher_displaymarks'),
    path('search_student1/', views.search_student1, name='search_student1'),
]