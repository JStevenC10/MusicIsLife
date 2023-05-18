from django.db import models
from django.contrib.auth.models import User


# Create your models here.

genders = (
    ('RAP', 'rap'),
    ('ROCK', 'rock'),
    ('REGAETTON', 'regaeton'),
    ('REGGUE', 'reggue'),
    ('BALADAS', 'baladas'),
    ('SALSA', 'salsa'),
    ('SALSA-CHOKE', 'salsa-choke'),
    ('BACHATA', 'bachata'),
    ('COUNTRY', 'country')
)



class Song(models.Model):
    photo = models.ImageField(null=True, blank=True)
    artist = models.CharField(max_length=100)
    song = models.CharField(max_length=100)
    duration = models.FloatField()
    gender = models.CharField(max_length=50, choices=genders, default='RAP')
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='songs')
    

    def __str__(self):
        text = f'{self.artist} - {self.song} - {self.gender}'
        return text
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    content = models.TextField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='song_n', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s comment - {self.song.song}"
