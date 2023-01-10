
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['email', 'username', 'password']

#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#             'password': forms.PasswordInput(attrs={'class':'form-control'})
#         }
    
class UserForm(UserCreationForm):
    email = forms.EmailField()
    field_order = ['email', 'username', 'password1', 'password2']
    


    
