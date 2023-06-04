from django.urls import reverse

from students.cities import CITIES
from django.db import models

from django.utils.text import slugify


class Group(models.Model):
    group_number = models.CharField(max_length=10, unique=True, null=True, blank=True)

    def get_url(self):
        return reverse('students:show_students_list_page', args=[self.group_number])


    def __str__(self):
        return f'{self.group_number}'

class AntisocialBehavior(models.Model):
    date = models.DateField(null=False, blank=False, verbose_name='Дата')
    character = models.TextField(null=False, blank=False, verbose_name='Характер проявления')
    meri = models.TextField(null=False, blank=False, verbose_name='Меры')
    result = models.TextField(null=False, blank=False, verbose_name='Результат')


class SpecialistRecomendations(models.Model):
    recomendations = models.TextField(null=False, blank=False, verbose_name='Рекомендации')
    result = models.TextField(null=False, blank=False, verbose_name='Результат')


class Incentives(models.Model):
    date = models.DateField(null=False, blank=False, verbose_name='Дата')
    achievements = models.TextField(null=False, blank=False, verbose_name='За какие достижения')
    form_of_incentives = models.TextField(null=False, blank=False, verbose_name='Форма поощрения')


class IndividualWork(models.Model):
    date = models.DateField(null=False, blank=False, verbose_name='Дата')
    content = models.TextField(null=False, blank=False, verbose_name='Содержание работы')
    result = models.TextField(null=False, blank=False, verbose_name='Результат')


class WorkWithParents(models.Model):
    date = models.DateField(null=False, blank=False, verbose_name='Дата')
    content = models.TextField(null=False, blank=False, verbose_name='Содержание работы')
    result = models.TextField(null=False, blank=False, verbose_name='Результат')


class Student(models.Model):
    OFF_BUDGET = 'Off-budget'
    BUDGET = 'Budget'
    FULL = 'Full'
    NOT_FULL = 'Not full'
    SEX_CHOICES = [
        ('Male', 'Мужской'),
        ('Female', 'Женский'),
    ]
    TYPE_EDUCATION_CHOICE = [
        (BUDGET, 'Бюджет'),
        (OFF_BUDGET, 'Внебюджет'),
    ]
    SUBMIT_CHOICES = [
        ('YES', 'Да'),
        ('NO', 'Нет'),
    ]
    TYPE_OF_FAMILY_CHOICES = [
        (FULL, 'Полная'),
        (NOT_FULL, 'Неполная'),
    ]
    group_number = models.ForeignKey(
        Group, on_delete=models.CASCADE, db_column='group_number', db_constraint=False, to_field='group_number')
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    otchestvo = models.CharField(max_length=128)
    image = models.ImageField(upload_to='student_images', blank=True)
    dateBirth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=128,choices=CITIES, null=True, blank=True)
    sex = models.CharField(max_length=16, null=True, choices=SEX_CHOICES, blank=True)
    education_type = models.CharField(max_length=16, null=True, choices=TYPE_EDUCATION_CHOICE, blank=True)
    hostel = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    foreigner = models.CharField(max_length=16, null=True, choices=SUBMIT_CHOICES, blank=True)
    type_of_family = models.CharField(max_length=16, null=True, choices=TYPE_OF_FAMILY_CHOICES, blank=True)
    family_large = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    guardianship = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    family_foster = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    low_income_family = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    refugees = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    settlers = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    family_students = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    have_children_students = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    upo_students = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    ngz_students = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    sop = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    ipr = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    orphan_students = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    brsm = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    prof_souz = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    self_government_student = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    invalid = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    oprf = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    circle = models.CharField(max_length=3, null=True, choices=SUBMIT_CHOICES, blank=True)
    antisocial_behavior = models.ManyToManyField(AntisocialBehavior)
    specialist_recommendations = models.ManyToManyField(SpecialistRecomendations, blank=True)
    incentives = models.ManyToManyField(Incentives, blank=True)
    individualwork = models.ManyToManyField(IndividualWork, blank=True)
    workwithparents = models.ManyToManyField(WorkWithParents, blank=True)
    citizenship = models.CharField(max_length=32, null=True, blank=True)
    health = models.TextField(null=True, blank=True)
    hobbies = models.TextField(null=True, blank=True)
    conditions = models.TextField(null=True, blank=True)
    other_info = models.TextField(null=True, blank=True)
    place_living = models.CharField(max_length=128, null=True, blank=True)

    def get_url(self):
        return reverse('students:show_info_about_student', args=[self.group_number,self.last_name])

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.otchestvo}'
