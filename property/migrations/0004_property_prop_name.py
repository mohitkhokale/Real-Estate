# Generated by Django 4.0.3 on 2022-03-28 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_alter_property_agent_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='prop_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]