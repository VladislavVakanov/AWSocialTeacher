from django import forms

from students.models import (Student, AntisocialBehavior, SpecialistRecomendations,
                             Incentives, IndividualWork, WorkWithParents)
from students.cities import CITIES_FOR_FORM


class StudentForm(forms.ModelForm):
    OFF_BUDGET = 'UNBUDGET'
    BUDGET = 'BUDGET'
    FULL = 'FULL'
    NOT_FULL = 'NOTFULL'
    SEX_CHOICES = [
        ('', '---------'),
        ('MALE', 'Мужской'),
        ('FEMALE', 'Женский'),
    ]
    TYPE_EDUCATION_CHOICE = [
        ('', '---------'),
        (BUDGET, 'Бюджет'),
        (OFF_BUDGET, 'Внебюджет'),
    ]
    SUBMIT_CHOICES = [
        ('', '---------'),
        ('YES', 'Да'),
        ('NO', 'Нет'),
    ]
    TYPE_OF_FAMILY_CHOICES = [
        ('', '---------'),
        (FULL, 'Полная'),
        (NOT_FULL, 'Неполная'),
    ]
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input'
    }), required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input'
    }), required=False)
    otchestvo = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input'
    }), required=False)
    dateBirth = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-date-picker',
        'placeholder': '00.00.0000',
        'pattern': '\d{2}\.\d{2}\.\d{4}',
        'title': 'Введите дату рождения 00.00.0000'
    }), required=False)
    address = forms.ChoiceField(choices=CITIES_FOR_FORM, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    sex = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field'
    }), required=False)
    education_type = forms.ChoiceField(choices=TYPE_EDUCATION_CHOICE, widget=forms.Select(attrs={
        'class': 'form-choice-field'
    }), required=False)
    hostel = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field'
    }), required=False)
    foreigner = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field'
    }), required=False)
    type_of_family = forms.ChoiceField(choices=TYPE_OF_FAMILY_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field'
    }), required=False)
    family_large = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    guardianship = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    family_foster = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    low_income_family = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    refugees = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    settlers = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    family_students = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    have_children_students = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    upo_students = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    ngz_students = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    sop = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    ipr = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    orphan_students = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)

    lica_iz_chisla_detei = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    deti = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    lica_iz_detei = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)

    brsm = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    prof_souz = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    self_government_student = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    invalid = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    oprf = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    circle = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-image-input'
    }), required=False)
    citizenship = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input'
    }), required=False)
    health = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-text-area'
    }), required=False)
    hobbies = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-text-area'
    }), required=False)
    conditions = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-text-area'
    }), required=False)
    other_info = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-text-area'
    }), required=False)
    place_living = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input'
    }), required=False)

    class Meta:
        model = Student
        fields = ('last_name', 'first_name', 'otchestvo', 'image', 'dateBirth', 'address', 'sex', 'education_type',
                  'hostel', 'foreigner', 'type_of_family', 'family_large', 'guardianship', 'family_foster',
                  'low_income_family', 'refugees', 'settlers', 'family_students', 'have_children_students',
                  'upo_students', 'ngz_students', 'sop', 'ipr', 'orphan_students', 'lica_iz_chisla_detei',
                  'deti', 'lica_iz_detei', 'brsm', 'prof_souz', 'self_government_student', 'invalid', 'oprf', 'circle',
                  'citizenship', 'health', 'hobbies', 'conditions', 'other_info', 'place_living')


class AntisocialBehaviorForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-date-picker',
        'type': 'date'
    }))
    character = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-text-area'
    }))
    meri = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-text-area'
    }))
    result = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-text-area'
    }))
    class Meta:
        model = AntisocialBehavior
        fields = ('date', 'character', 'meri', 'result')


class SpecialistRecomendationsForm(forms.ModelForm):
    recomendations = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-text-area'
    }))
    result = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-text-area'
    }))
    class Meta:
        model = SpecialistRecomendations
        fields = ('recomendations', 'result')


class IncentivesForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-date-picker',
        'type': 'date'
    }))
    achievements = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-text-area'
    }))
    form_of_incentives = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-text-area'
    }))
    class Meta:
        model = Incentives
        fields = ('date', 'achievements', 'form_of_incentives')


class IndividualWorkForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-date-picker',
        'type': 'date'
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-text-area'
    }))
    result = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-text-area'
    }))
    class Meta:
        model = IndividualWork
        fields = ('date', 'content', 'result')


class WorkWithParentsForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-date-picker',
        'type': 'date'
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-text-area'
    }))
    result = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-text-area'
    }))
    class Meta:
        model = WorkWithParents
        fields = ('date', 'content', 'result')