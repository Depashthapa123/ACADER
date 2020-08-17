from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from students.models import CustomUser, Course, Marks, Terms, Grade, Faculty


def teacher_profile(request):
    return render(request, 'teacherinterface/teacher_profile.html')


def teacher_dashboard(request):
    return render(request, 'teacherinterface/teacher_dashboard.html')


def teacher_marks(request):
    students = CustomUser.objects.filter(user_type=3)
    return render(request, 'teacherinterface/teacher_marks.html', {'students': students})


def do_logout1(request):
    logout(request)
    return redirect('loginpage')