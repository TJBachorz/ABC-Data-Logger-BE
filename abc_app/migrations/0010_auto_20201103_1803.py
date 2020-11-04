# Generated by Django 3.1.2 on 2020-11-03 18:03

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abc_app', '0009_auto_20201101_1809'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=60, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='case',
            name='accounts',
            field=models.ManyToManyField(related_name='cases', through='abc_app.CaseLink', to=settings.AUTH_USER_MODEL),
        ),
    ]
