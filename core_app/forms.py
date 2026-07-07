from django import forms
from .models import File

class uploadPDFForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ["docfile"]
