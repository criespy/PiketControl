from django import forms
from .models import *
from django.forms import ModelForm

TRUE_FALSE_CHOICES = [
    (True, 'True'),
    (False, 'False'),
]

class CpInputForm(ModelForm):
    mp_jumlah = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, widget=forms.RadioSelect)
    mp_pos = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, widget=forms.RadioSelect)
    material_jumlah = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, widget=forms.RadioSelect)
    material_std = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, widget=forms.RadioSelect)
    mesin_normal = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, widget=forms.RadioSelect)
    metode_sesuai = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, widget=forms.RadioSelect)
    plan_vs_actual = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, widget=forms.RadioSelect)
    environment_aman = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = CpInputModel
        fields = '__all__'
  