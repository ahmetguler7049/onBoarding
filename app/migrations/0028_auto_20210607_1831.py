# Generated by Django 3.1.7 on 2021-06-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20210607_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='is_tech_exist',
            field=models.CharField(choices=[('Var', 'Var'), ('Yok', 'Yok')], max_length=250, null=True, verbose_name='Teknik Üye Var mı'),
        ),
    ]