from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Course, StudentCourse, Terms, Marks


class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser, UserModel)
admin.site.register(StudentCourse)
admin.site.register(Course)
admin.site.register(Terms)
admin.site.register(Marks)
