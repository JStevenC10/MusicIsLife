from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse    

from .forms import UserForm, ProfileForm
from musicApp.views import home, my_songs

from django.http import HttpResponse

from .models import Profile


# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to=my_songs)
        else:
            return redirect(to=signup)
    else:
        form = UserForm()
        return render(request, 'register.html', {'form':form})
    
def profile(request):
    upd_profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(instance=upd_profile, data=request.POST)
        if form.is_valid():
            upd_profile = form.save(commit=False)
            if request.FILES:
                upd_profile.image = request.FILES['image']
                upd_profile.save()
            upd_profile.save()
            return redirect(to=profile)
    else:
        form = ProfileForm(instance=upd_profile)    
    context = {
        'form': form
    }
    return render(request, 'profile.html', context)
   


def deslogin(request):
    logout(request)
    return redirect(to=home)

