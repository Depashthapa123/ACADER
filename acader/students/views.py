
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from teacherinterface.models import postmessage
from .models import CustomUser, Course, Marks, Terms, Grade, Faculty, StudentCourse, Student, Teacher
from .restrictions import unauthenticated_admin, unauthenticated_teacher, unauthenticated_student, login_authenticate


@login_authenticate
def loginpage(request):
    # userType = 3
    #
    # if request.method == 'GET':
    #     if 'user-type' in request.COOKIES:
    #         # userType = request.COOKIES['user-type']
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        userType = str(request.POST['user-type'])

        user = authenticate(username=username,password=password)

        # request.COOKIES['user'] = user.id
        # request.COOKIES['user-type'] = userType

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
def teacherregister(request):

    if request.method == 'POST':
        name = request.POST['username']
        first_name = (request.POST['first_name']).capitalize()
        last_name = (request.POST['last_name']).capitalize()
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        gender = request.POST['gender']
        address = (request.POST['address']).capitalize()
        contact = request.POST['contact']
        faculty = request.POST['faculty']
        grade = request.POST['grade']
        section = request.POST['section']

        if len(first_name)>10 :
            messages.warning(request,"First name must contain 10 alphabets")
            return redirect("teacherregister") 

        if len(last_name)>10 :
            messages.warning(request,"Last name must contain 10 alphabets")
            return redirect("teacherregister")

        if not first_name.isalpha():
            messages.warning(request,"Enter your first name correctly! Must only contain albhabets")
            return redirect("teacherregister")

        if not last_name.isalpha():
            messages.warning(request,"Enter your last name correctly! Must only contain albhabets")
            return redirect("teacherregister") 

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,"This username already exists")
            return redirect("teacherregister")

        if len(username)>10:
            messages.warning(request,"The username is too long")
            return redirect("teacherregister")

        if not username.isalnum():
            messages.warning(request,"Invalid username registered")
            return redirect("teacherregister") 

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,"This email already exists")
            return redirect("teacherregister")   

        if not contact.isnumeric():
            messages.warning(request,"The contact number should only contain numeric value")
            return redirect("teacherregister")                      

        if len(address)>15:
            messages.warning(request,"Address should contain maximum of 15 characters")
            return redirect("teacherregister")

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
        # return redirect('teacher-func')

    return render(request, 'students/teacherregister.html')


@unauthenticated_admin
def studentregister(request):

    if request.method == 'POST':
        name = request.POST['username']
        first_name = (request.POST['first_name']).capitalize()
        last_name = (request.POST['last_name']).capitalize()
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        gender = request.POST['gender']
        DOB = request.POST['DOB']
        parent_name = (request.POST['parent_name']).capitalize()
        address = (request.POST['address']).capitalize()
        contact = request.POST['contact']
        faculty = request.POST['faculty']
        grade = request.POST['grade']
        section = request.POST['section']

        if len(first_name)>10:
            messages.warning(request,"First name contain 10 alphabets")
            return redirect("studentregister")

        if len(last_name)>10:
            messages.warning(request,"Last name must contain 10 alphabets")
            return redirect("studentregister")

        if not first_name.isalpha():
            messages.warning(request,"Enter your first name correctly! Must only contain albhabets")
            return redirect("studentregister")

        if not last_name.isalpha():
            messages.warning(request,"Enter your last name correctly! Must only contain albhabets")
            return redirect("studentregister") 

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,"This username already exists")
            return redirect("studentregister")

        if len(username)>10:
            messages.warning(request,"The username is too long")
            return redirect("studentregister")

        if not username.isalnum():
            messages.warning(request,"Invalid username registered")
            return redirect("studentregister") 

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,"This email already exists")
            return redirect("studentregister")   

        if len(parent_name)>15:
            messages.warning(request,"The parent name is too long")
            return redirect("studentregister")

        if not contact.isnumeric():
            messages.warning(request,"The contact number should only contain numeric value")
            return redirect("studentregister")                      

        if len(address)>15:
            messages.warning(request,"Address should contain maximum of 15 characters")
            return redirect("studentregister")


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
        messages.success(request, 'A student is added')
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
        # return redirect('student-func')


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
    students_model = list(CustomUser.objects.filter(user_type=3))
    terms = Terms.objects.all()

    show_full_form = False

    if 'Select' in request.POST:
        student_id = request.POST['student-id']

        # fetching grade and faculty based on student id
        student_info = Student.objects.filter(student_id=student_id).values('grade', 'faculty')
        selected_student = filter(lambda student: student.id == int(student_id), list(students_model))

        student_grade = list(student_info)[0]['grade']
        student_faculty = list(student_info)[0]['faculty']
        courses = Course.objects.filter(faculty=student_faculty, grade=student_grade)
        # print(courses)

        show_full_form = True
        context = {
            'students_model': students_model,
            'selected_student': list(selected_student)[0],
            'student_grade': student_grade,
            'student_faculty': student_faculty,
            'terms': terms,
            'show_full_form': show_full_form,
            'course_subject': courses,
        }
        return render(request, 'students/marks.html', context)

    elif 'Register' in request.POST:
        student_id = request.POST['student-id']
        grade = request.POST['grade']
        faculty = request.POST['faculty']
        term_id = request.POST['term']
        course = request.POST['course']
        obtained_marks = '{:0>2}'.format(request.POST['obtained_marks'])

        marks = Marks(
            obtained_marks=obtained_marks,
            terms_id=term_id,
            student_id=student_id,
            course=course,
            grade=grade,
            faculty=faculty,
        )
        marks.save()
        messages.success(request, "A student's marks is successfully added ")
    
        # return redirect('studentregister')


        # print('Registering')

    context = {'students_model': students_model, 'show_full_form': show_full_form}
    return render(request, 'students/marks.html',context)

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
    students_model = CustomUser.objects.filter(user_type=3).values('id')
    if request.method == 'POST':
        student_id = Student.objects.filter(student_id=students_model[0]['id']).values('faculty', 'grade')
        course_subject = Course.objects.filter(grade=student_id[0]['grade'], faculty=student_id[0]['faculty'])
        # course_id = request.POST['courses']
        # courses = Course.objects.get(id=course_id)


        # studentcourse1 = StudentCourse(
        #     student_id=student,
        #     course_id=courses,
        # )
        # studentcourse1.save()
        # messages.success(request, 'welldone ma boy')

    return render(request, '',
                  {'courses_model': courses_model,
                   'students_model': students_model,
                   'course_subject': course_subject,
                   })


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

@unauthenticated_admin
def edit_teacher(request,teacher_id_slug):
    teacher_slug = Teacher.objects.get(teacher=teacher_id_slug)

    if request.method == 'POST':
        teacher_id = request.POST['teacher_id']
        username = request.POST['username']
        address = (request.POST['address']).capitalize()
        faculty = request.POST['faculty']
        grade = request.POST['grade']
        section = request.POST['section']

        teacheruser = CustomUser.objects.get(id=teacher_id)
        teacheruser.username = username
        teacheruser.save()

        t_model = Teacher.objects.get(teacher_id=teacher_id)
        t_model.address = address
        t_model.faculty = faculty
        t_model.grade = grade
        t_model.section = section
        t_model.name = username
        t_model.save()

        # msg_model = postmessage.objects.get(teacher_id_id=teacher_id)
        # msg_model.name = username
        # msg_model.save()

        messages.success(request, f'Successfully edited')
        return redirect('/edit_teacher/' + teacher_id_slug)

    return render(request, 'admininterface/edit_teacher.html', {'teacher_slug': teacher_slug})


@unauthenticated_admin
def edit_student(request, student_id_slug):
    student_slug = Student.objects.get(student=student_id_slug)

    if request.method == 'POST':
        student_id = request.POST['student_id']
        username = request.POST['username']
        DOB = request.POST['DOB']
        parent_name = (request.POST['parent_name']).capitalize()
        address = (request.POST['address']).capitalize()
        contact = request.POST['contact']
        faculty = request.POST['faculty']
        grade = request.POST['grade']
        section = request.POST['section']

        studentuser = CustomUser.objects.get(id=student_id)
        studentuser.username = username
        studentuser.save()

        s_model = Student.objects.get(student_id=student_id)
        s_model.DOB = DOB
        s_model.parent_name = parent_name
        s_model.address = address
        s_model.contact = contact
        s_model.faculty = faculty
        s_model.grade = grade
        s_model.section = section
        s_model.name = username
        s_model.save()

        messages.success(request, f'Successfully edited')
        return redirect('/edit_student/' + student_id_slug)

    return render(request, 'admininterface/edit_student.html', {'student_slug': student_slug})


@unauthenticated_admin
def delete_teacher(request, teacher_del_slug):
    delete_teacher = CustomUser.objects.get(user_type=2, id=teacher_del_slug)
    print("DELETE===", delete_teacher)

    if request.method == 'POST':
        delete_teacher.delete()
        return redirect('teacher_list')

    return render(request, 'admininterface/delete_teacher.html', {'delete_teacher':delete_teacher})


@unauthenticated_admin
def delete_student(request, student_del_slug):
    delete_student = CustomUser.objects.get(user_type=3, id=student_del_slug)
    print("DELETE===", delete_student)

    if request.method == 'POST':
        delete_student.delete()
        return redirect('student_list')

    return render(request, 'admininterface/delete_student.html',{'delete_student':delete_student})