# Generated by Django 4.0.3 on 2022-03-30 10:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0035_alter_enquiry_date_of_inquiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='Gender',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='date_of_inquiry',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 30, 15, 32, 18, 923814)),
        ),
    ]
