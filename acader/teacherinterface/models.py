from django.db import models
from students.models import CustomUser, Student, Faculty, Grade, Teacher
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile1(models.Model):
    teacher = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    description = models.CharField(blank=False, max_length=500)

    def __str__(self):
        return f'{self.teacher.username} Profile'


@receiver(post_save, sender=CustomUser)
def create_teacher_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 2:
            Profile1.objects.create(teacher=instance)


@receiver(post_save, sender=CustomUser)
def save_teacher_profile(sender, instance, **kwargs):
    if instance.user_type == 2:
        instance.profile1.save()


class postmessage(models.Model):
    id = models.AutoField(primary_key=True)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=1)
    faculty = models.TextField(default=1)
    grade = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    message = models.CharField(blank=False, max_length=500)
    name = models.TextField(default=1)
    file_upload = models.FileField(upload_to='files/pdfs/', blank=True, null=True)

