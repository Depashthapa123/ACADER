# Generated by Django 3.1.1 on 2020-09-17 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherinterface', '0003_auto_20200915_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmessage',
            name='image_upload',
            field=models.ImageField(blank=True, null=True, upload_to='files/images'),
        ),
    ]
