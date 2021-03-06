# Generated by Django 4.0.3 on 2022-03-30 12:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0044_rename_gender_enquiry_requirement_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='userprofile',
        ),
        migrations.AddField(
            model_name='enquiry',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='date_of_inquiry',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 30, 17, 34, 36, 945778)),
        ),
    ]
