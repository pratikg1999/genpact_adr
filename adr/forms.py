from django import forms
from . import models

class prescription_form(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    gender = forms.IntegerField()
    disease = forms.CharField(max_length=100)
    medication = forms.CharField(max_length=100)
    naranjoFieldValue = forms.IntegerField()