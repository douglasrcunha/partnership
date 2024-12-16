from django import forms
from django.forms import ModelForm
from .models import Dashboard
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DasboardForm(ModelForm):
    class Meta:
        model = Dashboard
        fields = '__all__'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']        