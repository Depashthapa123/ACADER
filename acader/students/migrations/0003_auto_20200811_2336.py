# Generated by Django 3.0.7 on 2020-08-11 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20200811_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.TextField(),
        ),
    ]
