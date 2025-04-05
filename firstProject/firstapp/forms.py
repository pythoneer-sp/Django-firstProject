from django import forms
from .models import IITPStudent

class IITPStudentForm(forms.Form):
    item_s = forms.ModelChoiceField(queryset=IITPStudent.objects.all(), label="Select items name")