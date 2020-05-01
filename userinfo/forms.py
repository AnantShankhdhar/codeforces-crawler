from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=100,help_text='Required.')
    sur_name=forms.CharField(max_length=100,help_text='Required.')
    email=forms.CharField(max_length=200,help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'sur_name', 'email', 'password1', 'password2' )