from django.contrib import admin
from .models import Song, Comment

# Register your models here.

admin.site.register([Song, Comment])
