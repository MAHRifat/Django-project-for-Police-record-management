from django import forms
from .models import Authantication

class FormAuthantication(forms.ModelForm):
    class Meta:
        model = Authantication
        fields = '__all__'

    