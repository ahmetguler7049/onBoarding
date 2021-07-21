# Generated by Django 3.1.7 on 2021-05-23 11:57

import datetime
import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210523_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dogum_gunu',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 23, 14, 57, 48, 939406), verbose_name='Doğum Günü'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, null=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]