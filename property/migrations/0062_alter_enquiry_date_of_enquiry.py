# Generated by Django 4.0.3 on 2022-04-01 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0061_alter_enquiry_date_of_enquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='date_of_enquiry',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 1, 17, 4, 53, 846297)),
        ),
    ]
