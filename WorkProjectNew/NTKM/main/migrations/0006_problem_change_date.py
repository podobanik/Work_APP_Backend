# Generated by Django 4.2.14 on 2024-09-02 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_user_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='change_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения задачи'),
        ),
    ]
