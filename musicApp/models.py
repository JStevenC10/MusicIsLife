from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Song(models.Model):
    photo = models.ImageField(null=True, blank=True)
    artist = models.CharField(max_length=100)
    song = models.CharField(max_length=100)
    duration = models.FloatField()
    gender = models.CharField(max_length=50)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        text = f'{self.artist} - {self.song} - {self.gender}'
        return text
    
