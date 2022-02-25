from django import forms


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=100, min_length=6)
    last_name = forms.CharField(max_length=100, min_length=6)
    username = forms.CharField(max_length=36, min_length=6)
    password = forms.CharField(max_length=64, min_length=6)
    email = forms.EmailField(required=False)

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name
