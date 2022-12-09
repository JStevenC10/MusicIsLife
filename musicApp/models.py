from django.db import models

# Create your models here.

class Song(models.Model):
    artist = models.CharField(max_length=100)
    song = models.CharField(max_length=100)
    duration = models.FloatField()
    gender = models.CharField(max_length=50)
    link = models.CharField(max_length=300 )

    def __str__(self):
        text = f'{self.artist} - {self.song} - {self.gender}'
        return text
    
