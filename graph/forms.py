from django import forms
from .models import ExcelFile

class ExcelDataForm(forms.ModelForm):
    class Meta:
        model = ExcelFile
        fields = ['file']

class UploadFileForm(forms.Form):
    myFile = forms.FileField()


class UploadForm(forms.Form):
    excel_file = forms.FileField()




#test code
