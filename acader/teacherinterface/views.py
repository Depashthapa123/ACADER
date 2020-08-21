from django.shortcuts import render, redirect
from students.models import CustomUser, Course, Marks, Terms, Grade, Faculty, StudentCourse, Student, Teacher
from django.contrib.auth import login, authenticate, logout
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from .forms import BioUpdate1
from .models import postmessage
import sys


def teacher_profile(request):
    user2 = CustomUser.objects.get(user_type=2, id=request.user.id)
    if request.method == 'POST':
        # p_form = BioUpdate(request.POST, instance=request.user.profile)
        p_form = BioUpdate1(request.POST, request.FILES, instance=request.user.profile1)

        if p_form.is_valid():
            p_form.save()

            return redirect('teacher_profile')
    else:
        p_form = BioUpdate1(instance=request.user.profile1)
        # i_form = ImageUpdate(instance=request.user.profile)

    context = {
        'user2': user2,
        'p_form': p_form,
        # 'i_form': i_form
    }
    return render(request, 'teacherinterface/teacher_profile.html', context)


def teacher_dashboard(request):
    if request.session.has_key('teacher_id'):
        teacher_id = request.session['teacher_id']
    else:
        return redirect('teacherlogin/')

    if request.method == 'POST':
        requestParams = request.POST
        # print('teacher_id ', teacher_id)

        try:
            teacher = Teacher.objects.filter(teacher_id=teacher_id)
            teacher_faculty = Teacher.objects.filter(teacher_id=teacher_id).values('faculty')
            teacher_grade = Teacher.objects.filter(teacher_id=teacher_id).values('grade')
            teacher_createtime = Teacher.objects.filter(teacher_id=teacher_id).values('created_at')
            message = requestParams['message']
            name = Teacher.objects.filter(teacher_id=teacher_id).values('name')

            # print(teacher_faculty, teacher_grade)
            message = postmessage(
                teacher_id=teacher[0],
                faculty=teacher_faculty[0]['faculty'],
                grade=teacher_grade[0]['grade'],
                created_at=teacher_createtime[0]['created_at'],
                name=name,
                message=message,

            )
            # print(message)
            messagepostresponse = message.save()
            print('-------------------------------> ', messagepostresponse)
        except:
            print('An exception occured', sys.exc_info())

    return render(request, 'teacherinterface/teacher_dashboard.html')


def teacher_marks(request):
    teacher_id1 = None
    if request.session.has_key('teacher_id'):
        teacher_id1 = request.session['teacher_id']
    else:
        return redirect(request, 'teacherlogin/')

    teacher_faculty = Teacher.objects.filter(teacher_id=teacher_id1).values('faculty')
    teacher_grade = Teacher.objects.filter(teacher_id=teacher_id1).values('grade')
    # print(teacher_faculty[0]['faculty'], teacher_grade[0]['grade'])
    students = Student.objects.filter(faculty=teacher_faculty[0]['faculty'], grade=teacher_grade[0]['grade'])
    # print(students[0])
    return render(request, 'teacherinterface/teacher_marks.html', {'students': students})


def teacher_displaymarks(request, student_id):
    # students = Student.objects.filter(student_id=student_id)
    marks1 = Marks.objects.filter(student_id=student_id)
    return render(request, 'teacherinterface/teacher_displaymarks.html', {'marks1': marks1})


def do_logout1(request):
    logout(request)
    return redirect('loginpage')


# def postmessage(request):
#     user3 = CustomUser.objects.get(user_type=2, id=request.user.id)
#     teacher_id2 = None
#     if request.session.has_key('teacher_id'):
#         teacher_id2 = request.session['teacher_id']
#     else:
#         return redirect(request, 'teacherlogin/')
#     teacher_faculty1 = Teacher.objects.filter(teacher_id=teacher_id2).values('faculty')
#     teacher_grade1 = Teacher.objects.filter(teacher_id=teacher_id2).values('grade')
#     teacher_section = Teacher.objects.filter(teacher_id=teacher_id2).values('section')
#
#     if request.POST == 'POST':
#         m_form = Message(request.POST, request.FILES, instance=request.user.postmessage)
#
#         if m_form.is_valid():
#             m_form.save()
#             return redirect('teacher_dashboard/')
#         else:
#             m_form = Message(instance=request.user.postmessage)
#
#     return render(request, 'teacherinterface/teacher_dashboard.html', {'students1': students1, 'm_form': m_form, 'user3': user3})
#
