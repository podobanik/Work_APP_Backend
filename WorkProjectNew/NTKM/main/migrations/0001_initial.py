# Generated by Django 4.2.14 on 2024-08-20 03:20

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Адрес электронной почты')),
                ('second_name', models.CharField(max_length=50, verbose_name='Отчество')),
                ('title', models.CharField(max_length=50, verbose_name='Должность')),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name='Номер телефона')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='ObjectOfWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_of_work_text', models.CharField(max_length=200, verbose_name='Объект производства работ')),
            ],
            options={
                'verbose_name': 'Объект АСУТП',
                'verbose_name_plural': 'Объекты АСУТП',
            },
        ),
        migrations.CreateModel(
            name='ProblemStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_status_text', models.CharField(max_length=200, verbose_name='Статус выполнения задачи')),
            ],
            options={
                'verbose_name': 'Статус задачи',
                'verbose_name_plural': 'Статусы задач',
            },
        ),
        migrations.CreateModel(
            name='ProblemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_type_text', models.CharField(max_length=200, verbose_name='Категория задачи')),
            ],
            options={
                'verbose_name': 'Категория задачи',
                'verbose_name_plural': 'Категории задач',
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector_text', models.CharField(max_length=200, verbose_name='Сектор сотрудника')),
            ],
            options={
                'verbose_name': 'Сектор',
                'verbose_name_plural': 'Секторы',
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_text', models.TextField(max_length=1000, verbose_name='Введите название задачи')),
                ('control_date', models.DateField(default=0, verbose_name='Контрольный срок')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления задачи')),
                ('object_of_work', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.objectofwork', verbose_name='Объект АСУТП')),
                ('problem_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.problemstatus', verbose_name='Выберите статус задачи')),
                ('problem_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.problemtype', verbose_name='Выберите тип мероприятия')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='sector_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.sector', verbose_name='Сектор сотрудника'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
