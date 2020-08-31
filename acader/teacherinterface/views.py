from django.shortcuts import render, redirect, get_object_or_404
from students.models import CustomUser, Course, Marks, Terms, Grade, Faculty, StudentCourse, Student, Teacher
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from .forms import BioUpdate1
from .models import postmessage
from students.restrictions import unauthenticated_teacher
import sys
from teacherinterface.models import Profile1



@unauthenticated_teacher
def teacher_profile(request):
    if request.session.has_key('teacher_id'):
        teacher_id1 = request.session['teacher_id']
    user2 = CustomUser.objects.get(user_type=2, id=request.user.id)
    description = Profile1.objects.filter(teacher_id= teacher_id1)

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
        'description' : description,
        # 'i_form': i_form
    }
    return render(request, 'teacherinterface/teacher_profile.html', context)


@unauthenticated_teacher
def teacher_dashboard(request):
    if request.session.has_key('teacher_id'):
        teacher_id = request.session['teacher_id']

    teacher = Teacher.objects.filter(teacher_id=teacher_id)[0]
    post_messages = postmessage.objects.filter(teacher_id=teacher)

    context = {'post_message': post_messages}
    # print(context)

    if request.method == 'POST':
        requestParams = request.POST
        # print('teacher_id ', teacher_id)

        try:
            teacher = Teacher.objects.filter(teacher_id=teacher_id)
            teacher_faculty = Teacher.objects.filter(teacher_id=teacher_id).values('faculty')
            teacher_grade = Teacher.objects.filter(teacher_id=teacher_id).values('grade')
            teacher_createtime = Teacher.objects.filter(teacher_id=teacher_id).values('created_at')
            message1 = requestParams['message']
            name = Teacher.objects.filter(teacher_id=teacher_id).values('name')

            # teacher2 = postmessage.objects.filter(faculty=teacher_faculty[0]['faculty'],
            #                                       grade=teacher_grade[0]['grade'], name=name[0]['name'])

            # print(teacher_faculty, teacher_grade)
            message = postmessage(
                teacher_id=teacher[0],
                faculty=teacher_faculty[0]['faculty'],
                grade=teacher_grade[0]['grade'],
                created_at=teacher_createtime[0]['created_at'],
                name=name,
                message=message1,

            )
            # print(message)
            messagepostresponse = message.save()
            print('-------------------------------> ', messagepostresponse)
        except:
            print('An exception occured', sys.exc_info())

    return render(request, 'teacherinterface/teacher_dashboard.html', context)


@unauthenticated_teacher
def teacher_marks(request):
    teacher_id1 = None
    if request.session.has_key('teacher_id'):
        teacher_id1 = request.session['teacher_id']

    teacher_faculty = Teacher.objects.filter(teacher_id=teacher_id1).values('faculty')
    teacher_grade = Teacher.objects.filter(teacher_id=teacher_id1).values('grade')
    # print(teacher_faculty[0]['faculty'], teacher_grade[0]['grade'])
    students = Student.objects.filter(faculty=teacher_faculty[0]['faculty'], grade=teacher_grade[0]['grade'])
    # print(students[0])
    return render(request, 'teacherinterface/teacher_marks.html', {'students': students})


@unauthenticated_teacher
def teacher_displaymarks(request, student_id):
    # students = Student.objects.filter(student_id=student_id)
    marks1 = Marks.objects.filter(student_id=student_id)
    return render(request, 'teacherinterface/teacher_displaymarks.html', {'marks1': marks1})


@unauthenticated_teacher
def delete_post(request, message_id):
    context = None

    if request.method == 'POST':
        message = postmessage.objects.filter(id=message_id)
        message.delete()
        context = {'message': message}
        return redirect('teacher_dashboard')

    return render(request, 'teacherinterface/delete.html', context)


def do_logout1(request):
    logout(request)
    return redirect('loginpage')


@unauthenticated_teacher
def search_student1(request):
    if request.session.has_key('teacher_id'):
        teacher_id1 = request.session['teacher_id']
    search = request.GET['query']
    # if len(search) == 0:
    #     return render(request, 'blog/search.html')
    if search:
        teacher_faculty = Teacher.objects.filter(teacher_id=teacher_id1).values('faculty')
        teacher_grade = Teacher.objects.filter(teacher_id=teacher_id1).values('grade')
        # print(teacher_faculty[0]['faculty'], teacher_grade[0]['grade'])
        list = Student.objects.filter(faculty=teacher_faculty[0]['faculty'], grade=teacher_grade[0]['grade'], student__username__icontains=search)
        context = {
            'list':list,
            'search':search
        }
        return render(request, 'teacherinterface/search_student1.html', context)
    else:
        return render(request, 'teacherinterface/search_student1.html')
