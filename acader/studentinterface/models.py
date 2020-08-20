from django.db import models
from students.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms


class Profile(models.Model):
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    description = models.CharField(blank=False, max_length=500)

    def __str__(self):
        return f'{self.student.username} Profile'


@receiver(post_save, sender=CustomUser)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 3:
            Profile.objects.create(student=instance)


@receiver(post_save, sender=CustomUser)
def save_student_profile(sender, instance, **kwargs):
    if instance.user_type == 3:
        instance.profile.save()



