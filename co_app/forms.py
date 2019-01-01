from django import forms
from django.contrib.auth.models import User




class SignupForm(forms.ModelForm):
  class Meta:
    model   = User
    fields  = ['username', 'password','first_name', 'last_name', 'email']
    widgets = {
      'username': forms.TextInput(attrs={
        'id': 'username',
        'placeholder': 'username',
        'required': True
      }),
      'password': forms.PasswordInput(attrs={
        'id': 'password',
        'placeholder': 'Enter your Password',
        'required': True
      }),
      'first_name': forms.TextInput(attrs={
        'id': 'first_name',
        'placeholder': 'Enter your first name',
        'required': True
      }),
      'last_name': forms.TextInput(attrs={
        'id': 'last_name',
        'placeholder': 'Enter your last name',
        'required': True
      }),
      'email': forms.EmailInput(attrs={
        'id': 'email',
        'placeholder': 'Enter your Email',
        'required': True
      })    
    }


class LoginForm(forms.ModelForm):
  class Meta:
    model   = User
    fields  = ['username', 'password']
    widgets = {
      'username': forms.TextInput(attrs={
        'id': 'login-username',
        'placeholder': 'username',
        'required': True
      }),
      'password': forms.PasswordInput(attrs={
        'id': 'password',
        'placeholder': 'Enter your Password',
        'required': True
      })  
    }


class ProfileForm(forms.ModelForm):
  class Meta:
    model   = User
    fields  = ['first_name', 'last_name']
    widgets = {
      'first_name': forms.TextInput(attrs={
        'id': 'profile-first_name',
        'placeholder': 'change your first name',
        'required': True
      }),
      'last_name': forms.TextInput(attrs={
        'id': 'profile-last_name',
        'placeholder': 'change your last name',
        'required': True
      })    
    }
 

