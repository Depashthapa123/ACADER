# Generated by Django 3.0.3 on 2021-04-24 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('description', models.CharField(max_length=500)),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='postmessage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('faculty', models.TextField(default=1)),
                ('grade', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('message', models.CharField(max_length=500)),
                ('name', models.TextField(default=1)),
                ('file_upload', models.FileField(blank=True, null=True, upload_to='files/pdfs/')),
                ('teacher_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.Teacher')),
            ],
        ),
    ]
