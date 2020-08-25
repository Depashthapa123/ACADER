from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Course, Marks, Terms, Grade, Faculty, StudentCourse, Student
from .restrictions import unauthenticated_admin, unauthenticated_teacher, unauthenticated_student, login_authenticate


@login_authenticate
def loginpage(request):
    # print(request.session.test_cookie_worked())
    # if request.session.has_key('username') and request.session.has_key('password'):
    #
    #     saved_username = request.session['username']
    #     saved_password = request.session['password']
    #
    #     user = authenticate(username=saved_username,password=saved_password)
    #
    #     if user is not None:
    #         login(request, user)
    #
    #         if user.user_type == '3':
    #             request.session['student_id'] = user.id
    #             return redirect('student_dashboard')
    #         elif user.user_type == '2':
    #             messages.warning(request, 'sory mf')
    #         else:
    #             messages.warning(request, 'sory mf')
    #             return redirect('loginpage')
    #     else:
    #         messages.warning(request, "invalid")
    #         return redirect('/')
    #     return
    # else:
    #     print('I do not have cookies')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        userType = str(request.POST['user-type'])

        user = authenticate(username=username,password=password)
        # print('userType is ', userType)
        # print(type(userType))
        # print('server userType is ', user.user_type)

        # print(userType == user.user_type)

        if user is not None:
            login(request, user)

            if userType == '1':
                if userType == user.user_type:
                    return redirect('student-func')
                else:
                    logout(request)
                    messages.warning(request, "invalid")
                    return redirect('/')
            elif userType == '2':
                if userType == user.user_type:
                    # print('redirecting to teacher')
                    request.session['teacher_id'] = user.id
                    return redirect('teacher_dashboard')
                else:
                    logout(request)
                    # print('redirecting to default')
                    messages.warning(request, "invalid")
                    return redirect('/')
            else:
                # print('in student function')
                if userType == user.user_type:
                    request.session['student_id'] = user.id
                    return redirect('student_dashboard')
                else:
                    logout(request)
                    # print('Not valid')
                    messages.warning(request, "invalid")
                    return redirect('/')
        else:
            messages.warning(request, "invalid")
            return redirect('/')
    else:
        return render(request, 'students/loginpage.html')


# @login_authenticate
# def teacherlogin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user1 = authenticate(username=username, password=password)
#         print('login as', user1)
#
#         if user1 is not None:
#             login(request, user1)
#             # print('ggwp', login2)
#             if user1.user_type == '2':
#                 request.session['teacher_id'] = user1.id
#                 return redirect('teacher_profile')
#             elif user1.user_type == '3':
#                 messages.warning(request, 'sorry ur not teacher')
#             else:
#                 messages.warning(request, 'sorry ur not a teacher')
#         else:
#             messages.warning(request, 'invalid')


@unauthenticated_admin
def register(request):

    if request.method == 'POST':
        name = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        gender = request.POST['gender']
        address = request.POST['address']
        contact = request.POST['contact']
        faculty = request.POST['faculty']
        grade = request.POST['grade']
        section = request.POST['section']

        user = CustomUser.objects.create_user(first_name=first_name,
                                              last_name=last_name,
                                              username=username,
                                              email=email,
                                              password=password,
                                              user_type=2)
        user.teacher.address = address
        user.teacher.name = name
        user.teacher.gender = gender
        user.teacher.contact = contact
        user.teacher.faculty = faculty
        user.teacher.grade = grade
        user.teacher.section = section

        user.save()
        messages.success(request, 'A teacher is added')
        return redirect('register')

    return render(request, 'students/register.html')


@unauthenticated_admin
def studentregister(request):

    if request.method == 'POST':
        name = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        gender = request.POST['gender']
        DOB = request.POST['DOB']
        parent_name = request.POST['parent_name']
        address = request.POST['address']
        contact = request.POST['contact']
        faculty = request.POST['faculty']
        grade = request.POST['grade']
        section = request.POST['section']

        user = CustomUser.objects.create_user(first_name=first_name,
                                              last_name=last_name,
                                              username=username,
                                              email=email,
                                              password=password,
                                              user_type=3)
        user.student.address = address
        user.student.name = name
        user.student.DOB = DOB
        user.student.parent_name = parent_name
        user.student.gender = gender
        user.student.contact = contact
        user.student.faculty = faculty
        user.student.grade = grade
        user.student.section = section

        hello = user.save()
        print(hello)
        messages.success(request, 'A teacher is added')
        return redirect('studentregister')

    return render(request, 'students/studentregister.html')


@unauthenticated_admin
def course(request):
    if request.method == 'POST':
        course_name = request.POST['course_name']
        faculty = request.POST['faculty']
        grade = request.POST['grade']
        pass_marks = request.POST['pass_marks']
        total_marks = request.POST['total_marks']

        course1 = Course(
            course_name=course_name,
            faculty=faculty,
            grade=grade,
            pass_marks=pass_marks,
            total_marks=total_marks,
        )
        course1.save()
        messages.success(request, "successful")

    return render(request, 'students/course.html')


@unauthenticated_admin
def terms(request):
    if request.method == 'POST':
        terms_name = request.POST['terms_name']

        term1 = Terms(
            terms_name=terms_name,
        )
        term1.save()
    return render(request, 'students/term.html')


@unauthenticated_admin
def grades(request):
    if request.method == 'POST':
        grade1 = request.POST['grade']

        grade2 = Grade(
            grade1=grade1
        )
        grade2.save()
    return render(request, 'students/grade.html')


@unauthenticated_admin
def facultys(request):
    if request.method == 'POST':
        faculty1 = request.POST['faculty']

        faculty2 = Faculty(
            faculty1=faculty1
        )
        faculty2.save()
    return render(request, 'students/faculty.html')


@unauthenticated_admin
def marks(request):
    if request.session.has_key('student_id'):
        student_id = request.session['student_id']
        print(student_id, 'found')
    else:
        print('not found')
    courses_model = Course.objects.all()
    students_model = CustomUser.objects.filter(user_type=3)
    terms_model = Terms.objects.all()
    grade_model = Grade.objects.all()
    faculty_model = Faculty.objects.all()
    if request.method == 'POST':
        obtained_marks = request.POST['obtained_marks']
        terms_id = request.POST['terms_name']
        term = Terms.objects.get(id=terms_id)
        student_id = request.POST['students']
        student = CustomUser.objects.get(id=student_id)
        course_id = request.POST['courses']
        courses = Course.objects.get(id=course_id)
        grade_id = request.POST['grade']
        grade = Grade.objects.get(id=grade_id)
        faculty_id = request.POST['faculty']
        faculty = Faculty.objects.get(id=faculty_id)

        marks1 = Marks(
            obtained_marks=obtained_marks,
            terms_id=term,
            student_id=student,
            course_id=courses,
            grade_id=grade,
            faculty_id=faculty
        )
        marks1.save()
        messages.success(request, 'mark is added')
    return render(request, 'students/marks.html',
                  {'courses_model': courses_model,
                   'students_model': students_model,
                   'terms_model': terms_model,
                   'grade_model': grade_model,
                   'faculty_model': faculty_model})


@login_required()
def home(request):
    return render(request, 'students/home.html')


@unauthenticated_admin
def student_func(request):
    if request.session.has_key('admin_id'):
        admin_id = request.session['admin_id']
        print(admin_id, 'found')
    else:
        print('not found')
    return render(request, 'students/student_func.html')


@unauthenticated_admin
def teacher_func(request):
    if request.session.has_key('admin_id'):
        admin_id = request.session['admin_id']
        print(admin_id, 'found')
    else:
        print('not found')
    return render(request, 'students/teacher_func.html')


def do_logout(request):
    logout(request)
    return redirect('loginpage')


@unauthenticated_admin
def studentcourse(request):
    courses_model = Course.objects.all()
    students_model = CustomUser.objects.filter(user_type=3)
    terms_model = Terms.objects.all()
    marks_model = Marks.objects.all()
    if request.method == 'POST':
        terms_id = request.POST['terms_name']
        term = Terms.objects.get(id=terms_id)
        student_id = request.POST['students']
        student = CustomUser.objects.get(id=student_id)
        course_id = request.POST['courses']
        courses = Course.objects.get(id=course_id)
        marks_id = request.POST['marks']
        mark = Grade.objects.get(id=marks_id)

        studentcourse1 = StudentCourse(
            terms_id=term,
            student_id=student,
            course_id=courses,
            marks_id=mark,
        )
        studentcourse1.save()
        messages.success(request, 'welldone ma boy')

    return render(request, '',
                  {'courses_model': courses_model,
                   'students_model': students_model,
                   'terms_model': terms_model,
                   'marks_model': marks_model})


@unauthenticated_admin
def student_list(request):
    students1 = CustomUser.objects.filter(user_type=3)
    return render(request, 'admininterface/student_list.html', {'students1': students1})


@unauthenticated_admin
def student_displaymarks(request, student_id):
    students1 = CustomUser.objects.filter(user_type=3)
    marks1 = Marks.objects.filter(student_id=student_id)
    return render(request, 'admininterface/student_displaymarks.html', {'marks1': marks1, 'students1': students1})


@unauthenticated_admin
def teacher_list(request):
    teachers1 = CustomUser.objects.filter(user_type=2)
    return render(request, 'admininterface/teacher_list.html', {'teachers1': teachers1})


@unauthenticated_admin
def search_student(request):
    search = request.GET['query']
    # if len(search) == 0:
    #     return render(request, 'blog/search.html')
    if search:
        list = CustomUser.objects.filter(user_type=3, username__icontains=search)
        context = {
            'list':list,
            'search':search
        }
        return render(request, 'admininterface/search_student.html', context)
    else:
        return render(request, 'admininterface/search_student.html')


@unauthenticated_admin
def search_teacher(request):
    search = request.GET['query']
    # if len(search) == 0:
    #     return render(request, 'blog/search.html')
    if search:
        list = CustomUser.objects.filter(user_type=2, username__icontains=search)
        context = {
            'list':list,
            'search':search
        }
        return render(request, 'admininterface/search_teacher.html', context)
    else:
        return render(request, 'admininterface/search_teacher.html')