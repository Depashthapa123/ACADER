# Generated by Django 3.1 on 2020-08-31 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacherinterface', '0011_postmessage_picture_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmessage',
            name='picture_id',
        ),
    ]
