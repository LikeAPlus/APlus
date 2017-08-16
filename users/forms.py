from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, AuthenticationForm, UsernameField
from django import forms
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Username',
            'id': 'example-text-input'
        }
        self.fields['password1'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'example-text-input'
        }
        self.fields['password2'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Check Password',
            'id': 'example-text-input'
        }


class SigninForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Username',
            'id': 'example-text-input'
        }
        self.fields['password'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'example-text-input'
        }

    username = UsernameField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'autofocus': '',
            'placeholder': 'Username',
        }),
        label=''
    )
    password = forms.CharField(
        label=(""),
        strip=False,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
