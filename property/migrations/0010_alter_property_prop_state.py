# Generated by Django 4.0.3 on 2022-03-29 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_remove_property_doc_listed_property_prop_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='prop_State',
            field=models.CharField(blank=True, choices=[('', ''), ('Assam', 'Assam'), ('Maharashtra', 'Maharashtra'), ('Madhya_Pradesh', 'Madhya Pradesh'), ('West_Bengal', 'West Bengal')], default='Select State', max_length=20, null=True),
        ),
    ]