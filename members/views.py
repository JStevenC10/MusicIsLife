from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import UserForm
from musicApp.views import home

from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(to=home)
            else:
                return redirect(to=signin)
        else:
            return redirect(to=signin)          
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to=home)
        else:
            return redirect(to=signup)
    else:
        form = UserForm()
        return render(request, 'register.html', {'form':form})
    
def deslogin(request):
    logout(request)
    return redirect(to=home)

