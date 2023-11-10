from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username=forms.CharField (max_length=100, label= "username" )
    password=forms.CharField (max_length=100, label= "password", widget=forms.PasswordInput())

class Signupform(UserCreationForm):
    class Meta:
        model= User
        fields= ('username','first_name','last_name','email','password1','password2')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields=('address','bio','profile_pic')
