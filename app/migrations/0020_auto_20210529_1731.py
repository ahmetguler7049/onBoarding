# Generated by Django 3.1.7 on 2021-05-29 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20210527_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_teamleader',
            field=models.BooleanField(blank=True, null=True, verbose_name='Ekip Lideri'),
        ),
    ]
