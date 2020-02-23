from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from mainapp.models import Profile
from .models import Imag

class SignUpForm(UserCreationForm):    

    class Meta:
        model = Profile
        widgets = {
            'username' : forms.TextInput(attrs = {'placeholder': 'Username','class': 'name'}),
            'password' : forms.PasswordInput(attrs = {'placeholder': 'Password','class': 'password'}),
            'password1' : forms.PasswordInput(attrs = {'placeholder': 'Password','class': 'password'}),
            'password2' : forms.PasswordInput(attrs = {'placeholder': 'Password','class': 'password'}),
            'first_name' : forms.TextInput(attrs = {'placeholder': 'First Name','class': 'firstname'}),
            'last_name' : forms.TextInput(attrs = {'placeholder': 'Last Name','class': 'lastname'}),
            'email'    : forms.EmailInput(attrs = {'placeholder': 'E-Mail','class': 'email'}),
            'location'    : forms.TextInput(attrs = {'placeholder': 'Location','class': 'location'})
        }
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'location' )

class ImgForm(forms.ModelForm):
    class Meta:
        model = Imag
        fields = ('title', 'genre', 'description', 'images',)