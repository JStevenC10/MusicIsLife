

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import Song, genders, Comment
from .forms import CommentForm

from django.http import HttpResponse, JsonResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

class ReelsView(ListView):
    model = Song
    context_object_name = 'songs'
    template_name = 'reels.html'

    def get_queryset(self):
        return Song.objects.all()
    

@login_required
def my_songs(request):
    songs = Song.objects.filter(author=request.user)
    choices = genders
    return render(request, 'songs.html', {'songs':songs, 'choices':choices})

@login_required
def add_song(request):
    try:
        photo = request.FILES['photo']
    except:
        photo = None
    artist = request.POST['artist']
    song = request.POST['song']
    duration = float(request.POST['duration'])
    gender = request.POST['gender']
    song = Song.objects.create(
        photo = photo,
        artist = artist,
        song = song,
        duration = duration,
        gender = gender,
        author = request.user
    )
    return redirect(to=my_songs)

@login_required
def update(request, id):
    upd_song = Song.objects.get(id=id)
    if request.method == 'POST':
        try:
            photo = request.FILES['photo']
            upd_song.photo = photo
        except:
            pass
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

@login_required
def comments_s(request, pk):
    song = Song.objects.get(pk=pk)
    if request.method == 'GET':
        form = CommentForm()    
        comments = Comment.objects.filter(song=song)
        context = {'song': song, 'comments':comments, 'form':form}
        return render(request, 'comments.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            com = form.save(commit=False)
            com.user = request.user 
            com.song = song
            com.save()
            return redirect(to=comments_s, pk=song.id)
        else:
            return redirect('reels')

def delete_comment(request, pk):
    del_comment = Comment.objects.get(pk=pk)
    del_comment.delete()
    return redirect(comments_s, pk=del_comment.song.id)


@login_required
def delete(request, id):
    del_song = Song.objects.get(id=id)
    del_song.delete()
    return redirect(to=my_songs)


def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        title = request.POST['title']
        message = request.POST['message']
        send_mail(title, message, email, [settings.EMAIL_HOST_USER], fail_silently=False)
        return render(request, 'contact.html', {
            'message': 'email send successfully! THANKS YOU!'
        })

    return render(request, 'contact.html')