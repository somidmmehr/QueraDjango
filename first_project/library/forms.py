import django.forms
from django import forms
from first_app.models import *


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=100, min_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, min_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=36, min_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=64, min_length=6, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = Person.people.get(username=username)
        except Person.DoesNotExist:
            user = None
        if user:
            message = "This username already exists!"
            raise forms.ValidationError(message)
        else:
            return username
