# Generated by Django 3.0.7 on 2020-08-31 06:52
# Generated by Django 3.1 on 2020-08-31 06:43
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacherinterface', '0005_postmessage_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmessage',
            name='image_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='teacherinterface.Profile1'),
        ),
    ]
