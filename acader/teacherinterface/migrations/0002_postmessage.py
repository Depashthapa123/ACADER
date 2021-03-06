# Generated by Django 3.0.7 on 2020-08-21 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0015_auto_20200821_0955'),
        ('teacherinterface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='postmessage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=500)),
                ('faculty_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.Faculty')),
                ('grade_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.Grade')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
            ],
        ),
    ]
