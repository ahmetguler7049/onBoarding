# Generated by Django 3.1.7 on 2021-05-27 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_user_girisim_adi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_teamleader',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
