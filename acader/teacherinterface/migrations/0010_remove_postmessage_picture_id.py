# Generated by Django 3.1 on 2020-08-31 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacherinterface', '0009_auto_20200831_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmessage',
            name='picture_id',
        ),
    ]