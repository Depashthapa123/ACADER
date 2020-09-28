# Generated by Django 3.0.3 on 2020-09-28 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('teacherinterface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='postmessage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('faculty', models.TextField(default=1)),
                ('grade', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('message', models.CharField(max_length=500)),
                ('name', models.TextField(default=1)),
                ('teacher_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.Teacher')),
            ],
        ),
    ]
