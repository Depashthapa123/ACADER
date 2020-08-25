from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_student(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == '3':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_func


def unauthenticated_admin(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == '1':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_func


def unauthenticated_teacher(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == '2':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_func


def login_authenticate(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == '3':
            return redirect('student_dashboard')
        elif request.user.is_authenticated and request.user.user_type == '2':
            return redirect('teacher_dashboard')
        elif request.user.is_authenticated and request.user.user_type == '1':
            print('redirecting to admin page')
            return redirect('student-func')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func
