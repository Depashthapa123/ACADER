# Generated by Django 3.1 on 2020-08-22 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0016_merge_20200822_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
