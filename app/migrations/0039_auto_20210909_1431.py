# Generated by Django 3.1.7 on 2021-09-09 11:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_auto_20210828_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_header', models.CharField(max_length=350, verbose_name='Article Başlığı')),
                ('article_description', models.TextField(verbose_name='Article Açıklaması')),
                ('date_created', models.DateField(default=django.utils.timezone.now, verbose_name='Oluşturma Tarihi')),
                ('image_900', models.FileField(upload_to='article_images/', verbose_name='Article Image')),
                ('text', models.TextField(verbose_name='Yazı İçeriği')),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='sınıf',
            new_name='sinif',
        ),
    ]