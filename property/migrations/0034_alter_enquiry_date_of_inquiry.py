# Generated by Django 4.0.3 on 2022-03-30 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0033_enquiry_enquiry_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='date_of_inquiry',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 30, 15, 15, 17, 852242)),
        ),
    ]
