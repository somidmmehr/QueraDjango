from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.forms import CharField

from .models import Book, Profile


class BootstrapFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class BookForm(forms.ModelForm, BootstrapFormMixin):
    class Meta:
        model = Book
        exclude = []


class UserRegistration(forms.ModelForm, BootstrapFormMixin):
    country = forms.ChoiceField(choices=Profile.COUNTRY_CHOICES)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'country', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'required': 'true'}),
            'email': forms.TextInput(attrs={'type': 'email'}),
            'password': forms.TextInput(attrs={'type': 'password'})
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.data['password'])
        if commit:
            user.save()
            Profile.objects.create(user=user, country=self.data['country'])
        return user


class LoginForm(AuthenticationForm, BootstrapFormMixin):
    def confirm_login_allowed(self, user):
        pass
