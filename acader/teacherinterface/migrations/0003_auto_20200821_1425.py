# Generated by Django 3.0.7 on 2020-08-21 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0015_auto_20200821_0955'),
        ('teacherinterface', '0002_postmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmessage',
            name='faculty_id',
        ),
        migrations.RemoveField(
            model_name='postmessage',
            name='grade_id',
        ),
        migrations.RemoveField(
            model_name='postmessage',
            name='student_id',
        ),
        migrations.AddField(
            model_name='postmessage',
            name='faculty',
            field=models.TextField(default=1),
        ),
        migrations.AddField(
            model_name='postmessage',
            name='grade',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='postmessage',
            name='teacher_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.Teacher'),
        ),
    ]