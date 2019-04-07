from django import forms
from .models import Data

class NewDataForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = Data
        fields = ['text']

