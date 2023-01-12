
from django.contrib.auth.models import User
from django import forms    

class UserForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }



    
