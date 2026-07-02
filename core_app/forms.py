from django import forms

class uploadPDFUpdate(forms.Form):
    file = forms.FileField(label="Selecione o arquivo de tabelas em pdf")