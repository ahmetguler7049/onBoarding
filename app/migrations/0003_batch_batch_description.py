# Generated by Django 3.1.7 on 2021-10-15 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211014_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='batch_description',
            field=models.TextField(null=True, verbose_name='Batch Açıklaması'),
        ),
    ]
