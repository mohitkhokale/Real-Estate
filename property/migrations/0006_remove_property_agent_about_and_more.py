# Generated by Django 4.0.3 on 2022-03-29 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_property_agent_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='agent_about',
        ),
        migrations.RemoveField(
            model_name='property',
            name='agent_contact',
        ),
        migrations.RemoveField(
            model_name='property',
            name='agent_email',
        ),
        migrations.RemoveField(
            model_name='property',
            name='agent_name',
        ),
        migrations.RemoveField(
            model_name='property',
            name='prop_area',
        ),
        migrations.RemoveField(
            model_name='property',
            name='prop_description',
        ),
        migrations.RemoveField(
            model_name='property',
            name='prop_img',
        ),
        migrations.RemoveField(
            model_name='property',
            name='prop_name',
        ),
        migrations.RemoveField(
            model_name='property',
            name='prop_price',
        ),
    ]
