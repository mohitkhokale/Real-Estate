# Generated by Django 4.0.3 on 2022-03-28 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='user',
        ),
        migrations.AlterField(
            model_name='property',
            name='prop_price',
            field=models.IntegerField(),
        ),
    ]