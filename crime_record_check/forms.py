from django import forms
from .models import Record_entry_NID,Record_entry_DOB,SecureCodeModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm


class Record_entry_form_NID(forms.ModelForm):
    class Meta:
         model = Record_entry_NID
         fields = '__all__'

class Record_entry_form_DOB(forms.ModelForm):
    class Meta:
         model = Record_entry_DOB
         fields = '__all__'


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id' : 'required'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email',]
    
class SecureCodeModelForm(forms.ModelForm):
    class Meta:
        model = SecureCodeModel
        fields = ['secure_code']

class user_chagne_data(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name','last_name','email',]

class CustomAuthenticationForm(AuthenticationForm):
    # You can customize the form if needed
    pass

