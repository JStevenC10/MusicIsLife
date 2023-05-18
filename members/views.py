from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


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
    
def profile(request, pk):
    get_profile = Profile.objects.filter(pk=pk).first()
    if get_profile.user == request.user:
        if request.method == 'POST':
            form = ProfileForm(instance=get_profile, data=request.POST)
            if form.is_valid():
                get_profile = form.save(commit=False)
                if request.FILES:
                    get_profile.image = request.FILES['image']
                    get_profile.save()
                get_profile.save()
                return redirect(to=profile, pk=pk)
        else:
            form = ProfileForm(instance=get_profile)    
            context = {
                'form': form,
                'profile':get_profile
                }
            return render(request, 'profile.html', context)
    
    else:
        context = {'profile': profile} 
        return render(request, 'profile.html', context)


def deslogin(request):
    logout(request)
    return redirect(to=home)

