# Generated by Django 3.1.7 on 2021-05-25 10:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20210525_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dogum_gunu',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Doğum Günü'),
        ),
    ]