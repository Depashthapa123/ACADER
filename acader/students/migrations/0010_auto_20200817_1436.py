# Generated by Django 3.0.7 on 2020-08-17 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_remove_studentcourse_course_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcourse',
            name='course_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.Course'),
        ),
        migrations.AddField(
            model_name='studentcourse',
            name='marks_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.Marks'),
        ),
        migrations.AddField(
            model_name='studentcourse',
            name='term_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.Terms'),
        ),
    ]
