# Generated by Django 3.1.7 on 2021-05-31 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20210529_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='girisim_adi',
            new_name='team_size',
        ),
    ]