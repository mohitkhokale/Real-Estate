# Generated by Django 4.0.3 on 2022-03-31 03:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0058_alter_enquiry_date_of_enquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='date_of_enquiry',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 31, 8, 59, 59, 375834)),
        ),
    ]
