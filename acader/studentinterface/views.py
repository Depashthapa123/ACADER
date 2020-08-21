from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from students.models import CustomUser, Course, Marks, Terms, Grade, Faculty
from students.models import CustomUser, Marks, Course
from .forms import BioUpdate
from django.db.models import Q

def student_profile(request):
        user3 = CustomUser.objects.get(user_type=3, id=request.user.id)
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
            # 'i_form': i_form
        }
        return render(request, 'studentinterface/student_profile.html', context)


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
