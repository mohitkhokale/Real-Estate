# Generated by Django 4.0.3 on 2022-03-29 04:07

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0024_alter_property_prop_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='prop_features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('SWIMMING_POOL', 'SWIMMING POOL'), ('3_STORIES', '3 STORIES'), ('JOG_PATH 2', 'JOG PATH'), ('2_LAWN', '2 LAWN'), ('BIKE_PATH', 'BIKE PATH')], default=False, max_length=51, verbose_name='Features'),
        ),
    ]
