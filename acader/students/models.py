from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    user_type_data = ((1, "Admin"), (2, "Teacher"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default=0)
    teacher = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    contact = models.IntegerField(default=0)
    faculty = models.TextField()
    grade = models.CharField(max_length=10)
    section = models.CharField(max_length=5)
    gender = models.TextField()
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default=0)
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255)
    address = models.TextField()
    contact = models.CharField(max_length=100)
    DOB = models.DateField(null=True)
    section = models.CharField(max_length=5)
    grade = models.IntegerField(default=0)
    faculty = models.TextField(max_length=50)
    parent_name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()



class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.TextField()
    faculty = models.CharField(max_length=50)
    grade = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    pass_marks = models.IntegerField(default=0)
    total_marks = models.IntegerField(default=0)


class Terms(models.Model):
    id = models.AutoField(primary_key=True)
    terms_name = models.TextField()


class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    grade1 = models.IntegerField(default=0)


class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    faculty1 = models.TextField()


class Marks(models.Model):
    id = models.AutoField(primary_key=True)
    obtained_marks = models.IntegerField(default=0)
    terms_id = models.ForeignKey(Terms, on_delete=models.CASCADE, default=1)
    student_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    grade_id = models.ForeignKey(Grade, on_delete=models.CASCADE, default=1)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class StudentCourse(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    term_id = models.ForeignKey(Terms, on_delete=models.CASCADE, default=1)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    marks_id = models.ForeignKey(Marks, on_delete=models.CASCADE, default=1)


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Admin.objects.create(admin=instance)
        if instance.user_type == 2:
            Teacher.objects.create(teacher=instance)
        if instance.user_type == 3:
            Student.objects.create(student=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin.save()
    if instance.user_type == 2:
        instance.teacher.save()
    if instance.user_type == 3:
        instance.student.save()