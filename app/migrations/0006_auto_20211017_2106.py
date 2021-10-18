# Generated by Django 3.1.7 on 2021-10-17 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20211017_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firm',
            name='firm_logo_150',
        ),
        migrations.AddField(
            model_name='content',
            name='content_image',
            field=models.FileField(blank=True, help_text='Fotoğrafınızın boyutunun 150x150 olmasına dikkat edin', null=True, upload_to='article_images', verbose_name='Firma Logosu'),
        ),
        migrations.AddField(
            model_name='firm',
            name='firm_logo',
            field=models.FileField(blank=True, null=True, upload_to='article_images', verbose_name='Firma Logosu'),
        ),
    ]
