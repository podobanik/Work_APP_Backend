from django.contrib.auth.models import User
from django.db import models



# ТПР, ТСБ, СБИБ
class ProblemType(models.Model):
    def __str__(self):
        return self.problem_type_text

    class Meta:
        verbose_name = 'Категория задачи'
        verbose_name_plural = 'Категории задач'

    problem_type_text = models.CharField(max_length=200, verbose_name='Категория задачи')


# Наименование сектора
class Sector(models.Model):
    def __str__(self):
        return self.sector_text

    class Meta:
        verbose_name = 'Сектор'
        verbose_name_plural = 'Секторы'

    sector_text = models.CharField(max_length=200, verbose_name='Сектор сотрудника')


# Выполнено, не выполнимо, в работе
class ProblemStatus(models.Model):
    def __str__(self):
        return self.problem_status_text

    class Meta:
        verbose_name = 'Статус задачи'
        verbose_name_plural = 'Статусы задач'

    problem_status_text = models.CharField(max_length=200, verbose_name='Статус выполнения задачи')


# НПС, ТДП, РДП
class ObjectOfWork(models.Model):
    def __str__(self):
        return self.object_of_work_text

    class Meta:
        verbose_name = 'Объект АСУТП'
        verbose_name_plural = 'Объекты АСУТП'

    object_of_work_text = models.CharField(max_length=200, verbose_name='Объект производства работ')


# Таблица с сотрудниками отдела
class Staff(models.Model):
    def __str__(self):
        return self.staff_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    staff_name = models.CharField(max_length=200, verbose_name='ФИО сотрудника')
    sector_id = models.ForeignKey(Sector, null=True, on_delete=models.DO_NOTHING, verbose_name='Сектор сотрудника')


# Основной класс с задачами отдела
class Problem(models.Model):
    def __str__(self):
        return self.problem_text

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    problem_text = models.TextField(max_length=1000, verbose_name='Введите название задачи')
    staff = models.ForeignKey(Staff, blank=True, null=True, on_delete=models.PROTECT,
                              verbose_name='Ответственный сотрудник')
    problem_status = models.ForeignKey(ProblemStatus, blank=True, null=True, on_delete=models.PROTECT,
                                       verbose_name='Выберите статус задачи')
    object_of_work = models.ForeignKey(ObjectOfWork, blank=True, null=True, on_delete=models.PROTECT,
                                       verbose_name='Объект АСУТП')
    problem_type = models.ForeignKey(ProblemType, blank=True, null=True, on_delete=models.PROTECT,
                                     verbose_name='Выберите тип мероприятия')
    control_date = models.DateField(default=0, verbose_name='Контрольный срок')
    add_date = models.DateTimeField(auto_created=True, verbose_name='Дата добавления задачи')
    end_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата завершения задачи')
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.PROTECT)



