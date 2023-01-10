from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import UserForm

from django.http import HttpResponse

from musicApp.views import home, my_songs

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        try:
            User.objects.create_user(
                form.data.get('username'),
                form.data.get('email'),
                form.data.get('password1')
                )
            return redirect(to=login)
        except Exception as ex:
            print(ex)
            return redirect(to=register)
    else:
        form = UserForm()
        return render(request, 'register.html', {
            'form': form
        })

def login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            form = AuthenticationForm()
            return render(request, 'signin.html', {'form': form, 'error':'username or password incorrect'})
        else:
            login(user)
            return redirect(to=home)
        
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

