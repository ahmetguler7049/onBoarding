# Generated by Django 3.1.7 on 2021-11-11 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20211024_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiplequestion',
            name='is_required',
            field=models.BooleanField(default=False, verbose_name='Zorunlu Alan'),
        ),
        migrations.AddField(
            model_name='optionquestion',
            name='is_required',
            field=models.BooleanField(default=False, verbose_name='Zorunlu Alan'),
        ),
        migrations.AddField(
            model_name='textquestion',
            name='is_required',
            field=models.BooleanField(default=False, verbose_name='Zorunlu Alan'),
        ),
    ]
