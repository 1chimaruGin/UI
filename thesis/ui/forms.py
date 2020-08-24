from django import forms
from .models import csvFile


class csvForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = csvFile
        fields = ('csv', )