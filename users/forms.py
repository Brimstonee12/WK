
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email =  forms.EmailField(max_length=254)
    username =  forms.CharField(max_length=30, help_text='May contain a max of 20 characters', label='Username')
    password1 = forms.CharField(widget=forms.PasswordInput(),label='Password',help_text='May contain a min of 8 characters')
    password2 = forms.CharField(widget=forms.PasswordInput(),label='Retype Password',help_text='')



    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2' )
