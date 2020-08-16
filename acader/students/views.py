from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Course, Marks, Terms, Grade, Faculty


def loginpage(request):
    if request.session.has_key('student_id'):
        student_id = request.session['student_id']
        print(student_id, 'found')
    else:
        print('not found')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            if user.user_type == '3':
                request.session['student_id'] = user.id
                return redirect('home')
            elif user.user_type == '2':
                messages.warning(request, 'sory mf')
                return redirect('loginpage')
            else:
                messages.warning(request, 'sory mf')
                return redirect('loginpage')
        else:
            messages.warning(request, "invalid")
            return redirect('/')
    else:
        return render(request, 'students/loginpage.html')


def teacherlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user1 = authenticate(username=username, password=password)

        if user1 is not None:
            login(request, user1)
            if user1.user_type == '2':
                return redirect('home')
            elif user1.user_type == '3':
                messages.warning(request, 'sorry ur not teacher')
                return redirect('teacherlogin')
            else:
                messages.warning(request, 'sorry ur not a teacher')
                return redirect('teacherlogin')
        else:
            messages.warning(request, 'invalid')
            return redirect('teacherlogin')
    else:
        return render(request, 'students/teacherlogin.html')


def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user1 = authenticate(username=username, password=password)

        if user1 is not None:
            login(request, user1)
            if user1.user_type == '1':
                return redirect('student-func')
            elif user1.user_type == '3':
                messages.warning(request, 'sorry ur not teacher')
                return redirect('adminlogin')
            else:
                messages.warning(request, 'sorry ur not a teacher')
                return redirect('adminlogin')
        else:
            messages.warning(request, 'invalid')
            return redirect('adminlogin')
    else:
        return render(request, 'students/adminlogin.html')


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


def terms(request):
    if request.method == 'POST':
        terms_name = request.POST['terms_name']

        term1 = Terms(
            terms_name=terms_name,
        )
        term1.save()
    return render(request, 'students/term.html')


def grades(request):
    if request.method == 'POST':
        grade1 = request.POST['grade']

        grade2 = Grade(
            grade1=grade1
        )
        grade2.save()
    return render(request, 'students/grade.html')


def facultys(request):
    if request.method == 'POST':
        faculty1 = request.POST['faculty']

        faculty2 = Faculty(
            faculty1=faculty1
        )
        faculty2.save()
    return render(request, 'students/faculty.html')


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



def student_func(request):
    return render(request, 'students/student_func.html')


def teacher_func(request):
    return render(request, 'students/teacher_func.html')