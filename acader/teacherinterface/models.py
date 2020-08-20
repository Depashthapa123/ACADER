from django.db import models
from students.models import CustomUser
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
