from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from mainapp.models import Profile
from .models import Docs,FeedbacksImage
from admins.models import Imag

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'name'})),
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password'})),
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password'})),
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password'})),
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'firstname'})),
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'lastname'})),
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'email'})),
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'location'}))
    

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
            'location'    : forms.TextInput(attrs = {'placeholder': 'Location','class': 'location'}),
        }
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'location' )

class DocForm(forms.ModelForm):
    class Meta:
        model = Docs
        fields = ('document',)

class feedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbacksImage
        widgets = {
            'ratings' : forms.NumberInput(attrs = {'id': 'star2_input','name': 'rating'})
            }
        fields = ('ratings', 'comments',)