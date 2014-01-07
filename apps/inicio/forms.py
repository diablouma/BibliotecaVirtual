from django.contrib.auth.forms import UserCreationForm
from django import forms

__author__ = 'diablouma'


class UserForm(UserCreationForm):
    telefono = forms.IntegerField()