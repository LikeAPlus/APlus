from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, AuthenticationForm, UsernameField
from django import forms
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User



class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Check Password'


class SigninForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'USERNAME'

        }
        self.fields['password'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'PASSWORD'
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'class' : 'form-control',
            'placeholder' : 'Username',
            'id' : 'example-text-input'
        }
        self.fields['password'].widget.attrs = {
            'class' : 'form-control',
            'placeholder' : 'Password',
            'id' : 'example-text-input'
        }