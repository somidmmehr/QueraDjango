import django.forms
from django import forms
from django.forms import TextInput, PasswordInput, EmailInput

from first_app.models import *


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=100, min_length=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, min_length=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=36, min_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=64, min_length=6,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if Person.people.filter(username=username).exists():
            message = "This username already exists!"
            raise forms.ValidationError(message)
        else:
            return username


class SignUpForm2(forms.ModelForm):

    # first_name = forms.CharField(max_length=100, min_length=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_name = forms.CharField(max_length=100, min_length=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # username = forms.CharField(max_length=36, min_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # password = forms.CharField(max_length=64, min_length=6,
    #                            widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
    # email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'username', 'password', 'email']

    def clean(self):
        if Person.people.filter(username=self.cleaned_data['username']).exists():
            message = "This username already exists!"
            raise forms.ValidationError(message)
