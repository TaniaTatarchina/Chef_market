from django import forms

from account.models import Client


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'username', 'password', 'email', 'phone', 'address')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)
