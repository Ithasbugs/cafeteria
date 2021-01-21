from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(forms.Form): 
    first_name = forms.CharField(label="first name ",widget=forms.TextInput(),max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(),max_length=50)
    email = forms.CharField(widget=forms.TextInput(),max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(), min_length= 6,max_length=30)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), min_length= 6,max_length=30)