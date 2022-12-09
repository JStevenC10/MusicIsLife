from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all/songs/', views.my_songs, name='all_songs'),
    path('add_song/', views.add_song, name='add_song'),
    path('update/song/<int:id>/', views.update, name='update'),
    path('delete/song/<int:id>/', views.delete, name='delete'),
    path('contact/', views.contact, name='contact')
]
