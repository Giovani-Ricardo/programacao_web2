from django import forms
from .models import Subject, Webpage, AcessRecord


class FormWebpage(forms.ModelForm):
    class Meta:
        model = Webpage
        fields = "__all__"


class FormAcessRecord(forms.ModelForm):
    class Meta:
        model = AcessRecord
        fields = "__all__"
