
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms    

class UserForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        help_text = {k:'' for k in fields}
    
