
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email =  forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')



    class Meta:
        model = User
        fields = ('username', 'email', 'password1' )

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'password1': forms.PasswordInput(attrs={ 'class': 'form-control','placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={ 'class': 'form-control','placeholder': 'Password Again'}),
        }


# 'class': 'form-control',
