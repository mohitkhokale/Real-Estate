# Generated by Django 4.0.3 on 2022-03-29 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerregister',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='CustomerRegister', to=settings.AUTH_USER_MODEL),
        ),
    ]
