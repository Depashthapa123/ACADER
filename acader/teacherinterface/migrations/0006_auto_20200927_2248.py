# Generated by Django 3.1 on 2020-09-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherinterface', '0005_remove_postmessage_image_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmessage',
            name='file_upload',
            field=models.FileField(blank=True, null=True, upload_to='files/pdfs/'),
        ),
    ]
