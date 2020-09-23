from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from students.models import CustomUser, Marks, Course, Teacher, Student
from django.db.models import Q
from .forms import BioUpdate
from teacherinterface.models import postmessage, Profile1
from students.restrictions import unauthenticated_student
from studentinterface.models import Profile


@unauthenticated_student
def student_profile(request):
        if request.session.has_key('student_id'):
            student_id = request.session['student_id']
            print(student_id, 'found')
        else:
            return redirect('loginpage/')

        user3 = CustomUser.objects.get(user_type=3, id=request.user.id)
        description = Profile.objects.filter(student_id= student_id)
        if request.method == 'POST':
            # p_form = BioUpdate(request.POST, instance=request.user.profile)
            p_form = BioUpdate(request.POST, request.FILES, instance=request.user.profile)

            if p_form.is_valid():
                p_form.save()

                return redirect('student_profile')
        else:
            p_form = BioUpdate(instance=request.user.profile)
            # i_form = ImageUpdate(instance=request.user.profile)

        context = {
            'user3': user3,
            'p_form': p_form,
            'description': description,
            # 'i_form': i_form
        }
        return render(request, 'studentinterface/student_profile.html', context)


@unauthenticated_student
def course_content(request):
    if request.session.has_key('student_id'):
        student_id = request.session['student_id']

    student_details = Student.objects.filter(student_id=student_id).values('faculty', 'grade')
    teacher_filter = Teacher.objects.filter(faculty=student_details[0]['faculty'], grade=student_details[0]['grade']).values('teacher_id')
    print(teacher_filter)

    course_subject = Course.objects.filter(faculty=student_details[0]['faculty'], grade=student_details[0]['grade'])

    teacher_context = []
    for teacher in teacher_filter:
        teacher_filter1 = CustomUser.objects.filter(id=teacher['teacher_id']).values('first_name', 'last_name', 'email')
        teacher_details = {'First_name': teacher_filter1[0]['first_name'], 'Last_name': teacher_filter1[0]['last_name'], 'Email': teacher_filter1[0]['email']}
        teacher_context.append(teacher_details)

    print('teacher details=', teacher_context)

    context = {
        'teacher_context': teacher_context,
        'course_subject': course_subject
    }
    return render(request, 'studentinterface/course_content.html', context)


@unauthenticated_student
def student_dashboard(request):
    if request.session.has_key('student_id'):
        student_id = request.session['student_id']

    # print(student_id)

    student_faculty = Student.objects.filter(student_id=student_id).values('faculty')
    student_grade = Student.objects.filter(student_id=student_id).values('grade')

    dashboard_messages = postmessage\
        .objects.filter(faculty=student_faculty[0]['faculty'], grade=student_grade[0]['grade']).values('teacher_id', 'message', 'created_at', 'name', 'file_upload').order_by('-created_at')

    dashboard_context = []
    for messages in dashboard_messages:
        type = None
        extension = None
        file_name = None
        print(messages)
        custom_user_id = Teacher.objects.filter(id=messages['teacher_id']).values('teacher_id')
        teacher_image = Profile1.objects.filter(teacher_id=custom_user_id[0]['teacher_id']).values('image')
        if messages['file_upload'] != '':
            extension = messages['file_upload'].split('.')[1]
            file_name = messages['file_upload'].split('/')[2]
        if extension == 'pdf' or extension == 'docx':
            type = 'file'
        elif extension == 'jpg' or extension == 'png':
            type = 'image'

        message_details = {
                **messages,
                'profile_picture': teacher_image[0]['image'],
                'file_type': type,
                'file_name': file_name
            }
        dashboard_context.append(message_details)
        print(dashboard_context)

    context = {
        'dashboard_context': dashboard_context,
        'dashboard_messages': dashboard_messages
    }

    return render(request, 'studentinterface/student_dashboard.html', context)


@unauthenticated_student
def student_marks(request):
    student_id = None
    if request.session.has_key('student_id'):
        student_id = request.session['student_id']
        print(student_id, 'found')
    else:
        return redirect('loginpage/')

    marks = Marks.objects.filter(student_id=student_id)

    return render(request, 'studentinterface/student_marks.html', {'marks': marks})


@unauthenticated_student
def search_marks(request):
    student_id = None
    if request.session.has_key('student_id'):
        student_id = request.session['student_id']
        print(student_id, 'found')
    else:
        return redirect('loginpage/')

    search = request.GET['query']
    if search:
        marklist = Marks.objects.filter(Q(student_id=student_id, course_id__course_name__icontains=search) |
                                          Q(student_id=student_id, terms_id__terms_name__icontains=search))
        context = {
            'marklist': marklist,
            'search': search
        }
        return render(request, 'studentinterface/search_marks.html', context)
    else:
        return render(request, 'studentinterface/search_marks.html')


def do_logout2(request):
    logout(request)
    return redirect('loginpage')
