from django import forms
from django.contrib.auth.models import User
from .models import Ticket_User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators


class RedbusRegistration(forms.ModelForm):
    class Meta:
        model = Ticket_User
        fields = '__all__'


class SignupForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}
