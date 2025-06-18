from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(label='Username')
    email = forms.CharField(label='Email')
    password1 = forms.CharField(label='Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']