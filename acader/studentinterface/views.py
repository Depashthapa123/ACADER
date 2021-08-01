from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from students.models import CustomUser, Marks, Course, Teacher, Student
from django.db.models import Q

from students.models import Faculty, Grade
from .forms import BioUpdate
from teacherinterface.models import postmessage, Profile1
from students.restrictions import unauthenticated_student
from studentinterface.models import Profile
import pickle
import os
from django.conf import settings


@unauthenticated_student
def student_profile(request):
    if request.session.has_key('student_id'):
        student_id = request.session['student_id']
        print(student_id, 'found')
    else:
        return redirect('loginpage/')

    user3 = CustomUser.objects.get(user_type=3, id=request.user.id)
    description = Profile.objects.filter(student_id=student_id)
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
    teacher_filter = Teacher.objects.filter(faculty=student_details[0]['faculty'],
                                            grade=student_details[0]['grade']).values('teacher_id')
    print(teacher_filter)

    course_subject = Course.objects.filter(faculty=student_details[0]['faculty'], grade=student_details[0]['grade'])

    teacher_context = []
    for teacher in teacher_filter:
        teacher_filter1 = CustomUser.objects.filter(id=teacher['teacher_id']).values('first_name', 'last_name', 'email')
        teacher_details = {'First_name': teacher_filter1[0]['first_name'], 'Last_name': teacher_filter1[0]['last_name'],
                           'Email': teacher_filter1[0]['email']}
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

    dashboard_messages = postmessage \
        .objects.filter(faculty=student_faculty[0]['faculty'], grade=student_grade[0]['grade']).values('teacher_id',
                                                                                                       'message',
                                                                                                       'created_at',
                                                                                                       'name',
                                                                                                       'file_upload').order_by(
        '-created_at')

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


@unauthenticated_student
def initialize_prediction(request):
    student_id = None
    if request.session.has_key('student_id'):
        student_id = request.session['student_id']
        print(student_id, 'found')
    else:
        return redirect('loginpage/')

    students = Student.objects.filter(student_id=student_id)
    print(students)

    students_grade = Student.objects.filter(student_id=student_id).values('grade')
    print(students_grade)
    students_faculty = Student.objects.filter(student_id=student_id).values('faculty')
    print(students_faculty)

    return render(request, 'studentinterface/initialize_prediction.html',
                  {'students': students})


@unauthenticated_student
def initialize_prediction_term(request):
    student_id = None
    if request.session.has_key('student_id'):
        student_id = request.session['student_id']
        print(student_id, 'found')
    else:
        return redirect('loginpage/')

    students = Student.objects.filter(student_id=student_id)

    return render(request, 'studentinterface/initialize_prediction_term.html',
                  {'students': students})


@unauthenticated_student
def predict_third(request):
    return render(request, 'studentinterface/third_term_prediction.html')


@unauthenticated_student
def result_third(request):
    path = os.path.join(settings.MODELS, '11physics3rd.pkl')
    # if request.method == 'POST':
    student_id = request.GET["s_id"]
    assignment = request.GET["assignment"]
    attendance = request.GET["attendance"]
    first = request.GET["first"]
    gender = request.GET["gender"]
    second = request.GET["second"]

    student_id = int(student_id)
    assignment = int(assignment)
    attendance = int(attendance)
    first = float(first)
    second = float(second)
    gender = int(gender)

    fields = [student_id, assignment, attendance, first, second, gender]

    with open(path, 'rb') as file:
        model = pickle.load(file)
        print(">> ML Model ====> " + str(model))

    prediction_value = model.predict([fields])[0]
    final = "Your predicted final marks is: " + str(prediction_value)

    return render(request, "studentinterface/third_term_prediction.html",
                  {"final": final, "id": id, "assignment": assignment,
                   "attendance": attendance, "first": first,
                   "second": second,
                   "gender": gender})


@unauthenticated_student
def predict(request):
    return render(request, 'studentinterface/final_prediction.html')


@unauthenticated_student
def result(request):
    path = os.path.join(settings.MODELS, '11physics.pkl')
    # if request.method == 'POST':
    student_id = request.GET["s_id"]
    assignment = request.GET["assignment"]
    attendance = request.GET["attendance"]
    first = request.GET["first"]
    gender = request.GET["gender"]
    second = request.GET["second"]
    third = request.GET["third"]

    student_id = int(student_id)
    assignment = int(assignment)
    attendance = int(attendance)
    first = float(first)
    second = float(second)
    third = float(third)
    gender = int(gender)

    fields = [student_id, assignment, attendance, first, second, third, gender]

    with open(path, 'rb') as file:
        model = pickle.load(file)
        print(">> ML Model ====> " + str(model))

    prediction_value = model.predict([fields])[0]
    final = "Your predicted final marks is: " + str(prediction_value)

    return render(request, "studentinterface/final_prediction.html",
                  {"final": final, "id": id, "assignment": assignment,
                   "attendance": attendance, "first": first,
                   "second": second, "third": third,
                   "gender": gender})


@unauthenticated_student
def predict_second(request):
    return render(request, 'studentinterface/second_term_prediction.html')


@unauthenticated_student
def result_second(request):
    path = os.path.join(settings.MODELS, '11physics2nd.pkl')
    # if request.method == 'POST':
    student_id = request.GET["s_id"]
    assignment = request.GET["assignment"]
    attendance = request.GET["attendance"]
    first = request.GET["first"]
    gender = request.GET["gender"]

    student_id = int(student_id)
    assignment = int(assignment)
    attendance = int(attendance)
    first = float(first)
    gender = int(gender)

    fields = [student_id, assignment, attendance, first, gender]

    with open(path, 'rb') as file:
        model = pickle.load(file)
        print(">> ML Model ====> " + str(model))

    prediction_value = model.predict([fields])[0]
    final = "Your predicted final marks is: " + str(prediction_value)

    return render(request, "studentinterface/second_term_prediction.html",
                  {"final": final, "id": id, "assignment": assignment,
                   "attendance": attendance, "first": first,
                   "gender": gender})


def do_logout2(request):
    logout(request)
    return redirect('loginpage')
