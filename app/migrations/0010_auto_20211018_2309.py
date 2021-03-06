# Generated by Django 3.1.7 on 2021-10-18 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20211018_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='selection_q_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Dropdown Soru Sayısı'),
        ),
        migrations.AddField(
            model_name='survey',
            name='test_q_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Test Soru Sayısı'),
        ),
        migrations.AddField(
            model_name='survey',
            name='text_q_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Text Soru Sayısı'),
        ),
    ]
