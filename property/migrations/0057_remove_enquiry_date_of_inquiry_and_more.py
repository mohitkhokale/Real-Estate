# Generated by Django 4.0.3 on 2022-03-30 15:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0056_alter_enquiry_date_of_inquiry_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='date_of_inquiry',
        ),
        migrations.AddField(
            model_name='enquiry',
            name='date_of_enquiry',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 30, 21, 23, 56, 615758)),
        ),
    ]
