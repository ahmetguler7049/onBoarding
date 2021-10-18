# Generated by Django 3.1.7 on 2021-10-17 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211016_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firm',
            name='firm_logo_135',
        ),
        migrations.AddField(
            model_name='firm',
            name='firm_logo_150',
            field=models.FileField(blank=True, help_text='Fotoğrafınızın boyutunun 150x150 olmasına dikkat edin', null=True, upload_to='article_images', verbose_name='Firma Logosu'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image_900',
            field=models.FileField(help_text='Fotoğrafınızın boyutunun oranının 9:4 olmasına dikkat edin', upload_to='article_images', verbose_name='Article Image'),
        ),
    ]