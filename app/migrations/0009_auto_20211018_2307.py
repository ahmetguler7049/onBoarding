# Generated by Django 3.1.7 on 2021-10-18 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_content_content_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='selection_q_count',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='test_q_count',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='text_q_count',
        ),
    ]
