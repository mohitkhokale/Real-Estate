# Generated by Django 4.0.3 on 2022-03-30 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0026_property_prop_city_alter_property_prop_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_inquiry', models.DateTimeField(default=datetime.datetime(2022, 3, 30, 14, 34, 4, 19717))),
                ('requirement_type', models.CharField(max_length=255)),
            ],
        ),
    ]