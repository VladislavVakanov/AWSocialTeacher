from django import forms

from students.models import Student
from students.cities import CITIES_FOR_FORM


class StudentForm(forms.ModelForm):
    OFF_BUDGET = 'Off-budget'
    BUDGET = 'Budget'
    FULL = 'Full'
    NOT_FULL = 'Not full'
    SEX_CHOICES = [
        ('', '---------'),
        ('Male', 'Мужской'),
        ('Female', 'Женский'),
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
        'type': 'date'
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
    circles = forms.ChoiceField(choices=SUBMIT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-choice-field',
    }), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-image-input'
    }), required=False)

    class Meta:
        model = Student
        fields = ('last_name', 'first_name', 'otchestvo', 'image', 'dateBirth', 'address', 'sex', 'education_type',
                  'hostel', 'foreigner', 'type_of_family', 'family_large', 'guardianship', 'family_foster',
                  'low_income_family', 'refugees', 'settlers', 'family_students', 'have_children_students',
                  'upo_students', 'ngz_students', 'sop', 'ipr', 'orphan_students', 'brsm', 'prof_souz',
                  'self_government_student', 'invalid', 'oprf', 'circles')
