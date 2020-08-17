from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Course, StudentCourse, Terms, Marks, Faculty, Grade


class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser, UserModel)
admin.site.register(StudentCourse)
admin.site.register(Course)
admin.site.register(Terms)
admin.site.register(Marks)
admin.site.register(Grade)
admin.site.register(Faculty)


