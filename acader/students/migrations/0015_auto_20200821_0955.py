# Generated by Django 3.0.7 on 2020-08-21 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0014_merge_20200821_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]