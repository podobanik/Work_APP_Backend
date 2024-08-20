# Generated by Django 4.2.14 on 2024-08-20 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=150, unique=True, verbose_name='Адрес электронной почты'),
        ),
        migrations.AlterField(
            model_name='user',
            name='second_name',
            field=models.CharField(max_length=150, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Должность'),
        ),
    ]
