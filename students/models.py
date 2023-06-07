from django.db import models
from django.urls import reverse

from simple_history.models import HistoricalRecords


class Group(models.Model):
    group_number = models.CharField(max_length=10, unique=True, null=False, blank=False, verbose_name='Группа')

    def get_url(self):
        return reverse('students:show_students_list_page', args=[self.group_number])

    class Meta:
        verbose_name = "Учебная группа"
        verbose_name_plural = "Учебные группы"


    def __str__(self):
        return f'{self.group_number}'

class AntisocialBehavior(models.Model):
    date = models.DateField(null=False, blank=False, verbose_name='Дата')
    character = models.TextField(null=False, blank=False, verbose_name='Характер проявления')
    meri = models.TextField(null=False, blank=False, verbose_name='Меры')
    result = models.TextField(null=False, blank=False, verbose_name='Результат')

    def __str__(self):
        return f'Дата: {self.date}\n Характер проявления:{self.character} | Меры: {self.meri} | Результат: {self.result}'

    class Meta:
        verbose_name = "Асоциальное поведение"
        verbose_name_plural = "Асоциальное поведения"


class SpecialistRecomendations(models.Model):
    recomendations = models.TextField(null=False, blank=False, verbose_name='Рекомендации')
    result = models.TextField(null=False, blank=False, verbose_name='Результат')
    def __str__(self):
        return f'Рекомендации: {self.recomendations} | Результат: {self.result}'

    class Meta:
        verbose_name = "Рекомендация специалиста"
        verbose_name_plural = "Рекомендации специалистов"


class Incentives(models.Model):
    date = models.DateField(null=False, blank=False, verbose_name='Дата')
    achievements = models.TextField(null=False, blank=False, verbose_name='За какие достижения')
    form_of_incentives = models.TextField(null=False, blank=False, verbose_name='Форма поощрения')
    def __str__(self):
        return f'Дата: {self.date} | За какие достижения: {self.achievements} | Форма поощрения: {self.form_of_incentives}'

    class Meta:
        verbose_name = "Поощрение учащегося"
        verbose_name_plural = "Поощрения учащихся"


class IndividualWork(models.Model):
    date = models.DateField(null=False, blank=False, verbose_name='Дата')
    content = models.TextField(null=False, blank=False, verbose_name='Содержание работы')
    result = models.TextField(null=False, blank=False, verbose_name='Результат')
    def __str__(self):
        return f'Дата: {self.date} | Содержание работы: {self.content} | Результат: {self.result}'
    class Meta:
        verbose_name = f"Индивидуальная работа с учащимся"
        verbose_name_plural = "Индивидуальная работа с учащимися"


class WorkWithParents(models.Model):
    date = models.DateField(null=False, blank=False, verbose_name='Дата')
    content = models.TextField(null=False, blank=False, verbose_name='Содержание работы')
    result = models.TextField(null=False, blank=False, verbose_name='Результат')
    def __str__(self):
        return f'Дата: {self.date} | Содержание работы: {self.content} | Результат: {self.result}'

    class Meta:
        verbose_name = f"Работа с родителями учащегося"
        verbose_name_plural = "Работа с родителями учащихся"





class Student(models.Model):
    SEX_CHOICES = [
        ('MALE', 'Мужской'),
        ('FEMALE', 'Женский'),
    ]
    TYPE_EDUCATION_CHOICE = [
        ('BUDGET', 'Бюджет'),
        ('UNBUDGET', 'Внебюджет'),
    ]
    SUBMIT_CHOICES = [
        ('YES', 'Да'),
        ('NO', 'Нет'),
    ]
    TYPE_OF_FAMILY_CHOICES = [
        ('FULL', 'Полная'),
        ('NOTFULL', 'Неполная'),
    ]
    TYPE_OF_STUDENT = [
        ('STAROSTA', 'Староста'),
        ('ZAMSTAROSTA', 'Заместитель старосты'),
        ('STUDENT', 'Учащийся(ася)'),
    ]
    group_number = models.ForeignKey(
        Group, on_delete=models.CASCADE, db_column='group_number', db_constraint=False, to_field='group_number', verbose_name='Группа')
    last_name = models.CharField(max_length=128, verbose_name='Фамилия')
    first_name = models.CharField(max_length=128, verbose_name='Имя')
    otchestvo = models.CharField(max_length=128, verbose_name='Отчество')
    image = models.ImageField(upload_to='student_images', blank=True, verbose_name='Фотография')
    dateBirth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    phoneNumber = models.CharField(max_length=128, null=False, blank=True, default='Номер телефона')
    sex = models.CharField(max_length=16, null=False, choices=SEX_CHOICES, blank=True, default='Пол')
    education_type = models.CharField(max_length=16, null=False, choices=TYPE_EDUCATION_CHOICE, blank=True, default='Тип обучения')
    hostel = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='Проживает в общежитие')
    status = models.CharField(max_length=16, null=False, choices=TYPE_OF_STUDENT, blank=True, default='')
    type_of_family = models.CharField(max_length=16, null=False, choices=TYPE_OF_FAMILY_CHOICES, blank=True, default='')
    family_large = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    guardianship = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    family_foster = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    low_income_family = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    refugees = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    settlers = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    family_students = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    have_children_students = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    upo_students = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    ngz_students = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    sop = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    ipr = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    orphan_students = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    lica_iz_chisla_detei = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    deti = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    lica_iz_detei = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    brsm = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    prof_souz = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    self_government_student = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    invalid = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    oprf = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    circle = models.CharField(max_length=3, null=False, choices=SUBMIT_CHOICES, blank=True, default='')
    incentives = models.ManyToManyField(Incentives, blank=True)
    antisocial_behavior = models.ManyToManyField(AntisocialBehavior, blank=True)
    specialist_recommendations = models.ManyToManyField(SpecialistRecomendations, blank=True)
    individualwork = models.ManyToManyField(IndividualWork, blank=True)
    workwithparents = models.ManyToManyField(WorkWithParents,blank=True)
    citizenship = models.CharField(max_length=32, blank=True, default='')
    health = models.TextField(null=False, blank=True, default='')
    hobbies = models.TextField(null=False, blank=True, default='')
    conditions = models.TextField(null=False, blank=True, default='')
    other_info = models.TextField(null=False, blank=True, default='')
    place_living = models.CharField(max_length=128, null=False, blank=True, default='')
    history = HistoricalRecords()

    def get_url(self):
        return reverse('students:show_info_about_student', args=[self.group_number,self.last_name])

    def __str__(self):
        return f'{self.last_name} | {self.first_name} | {self.otchestvo}'

    class Meta:
        verbose_name = f"учащегося"
        verbose_name_plural = "Учащиеся"