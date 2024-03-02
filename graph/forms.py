from django import forms
from .models import ExcelFile

class ExcelDataForm(forms.ModelForm):
    class Meta:
        model = ExcelFile
        fields = ['file']