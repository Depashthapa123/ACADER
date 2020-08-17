from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from students.models import CustomUser, Course, Marks, Terms, Grade, Faculty


def student_profile(request):
    return render(request, 'studentinterface/student_profile.html')


def course_content(request):
    return render(request, 'studentinterface/course_content.html')


def student_dashboard(request):
    return render(request, 'studentinterface/student_dashboard.html')


def student_marks(request):
    # students = CustomUser.objects.filter(user_type=3)
    return render(request, 'studentinterface/student_marks.html')


def do_logout2(request):
    logout(request)
    return redirect('loginpage')
