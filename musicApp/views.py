from django.shortcuts import render, redirect
from .models import Song

# Create your views here.

def home(request):
    return render(request, 'home.html')

def my_songs(request):
    songs = Song.objects.all()
    return render(request, 'songs.html', {'songs':songs})

def add_song(request):
    artist = request.POST['artist']
    song = request.POST['song']
    duration = float(request.POST['duration'])
    gender = request.POST['gender']
    song = Song.objects.create(
        artist = artist,
        song = song,
        duration = duration,
        gender = gender
    )
    return redirect(to=my_songs)

def update(request, id):
    upd_song = Song.objects.get(id=id)
    if request.method == 'POST':
        artist = request.POST['artist']
        song = request.POST['song']
        duration = float(request.POST['duration'])
        gender = request.POST['gender']
        upd_song.artist = artist
        upd_song.song = song
        upd_song.duration = duration
        upd_song.gender = gender
        upd_song.save()
        return redirect(to=my_songs)
    else:
        return render(request, 'update_song.html', {'song' : upd_song})

def delete(request, id):
    del_song = Song.objects.get(id=id)
    del_song.delete()
    return redirect(to=my_songs)

def contact(request):
    return render(request, 'contact.html')