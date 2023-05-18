from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.staticfiles.urls import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all/songs/', views.my_songs, name='all_songs'),
    path('songs/reels/', login_required( views.ReelsView.as_view()), name='reels'),
    path('song/<int:pk>/comments/', views.comments_s, name='comments'),
    path('comment/<int:pk>/delete', views.delete_comment, name='delete_comment'),
    path('add_song/', views.add_song, name='add_song'),
    path('update/song/<int:id>/', views.update, name='update'),
    path('delete/song/<int:id>/', views.delete, name='delete'),
    path('contact/', views.contact, name='contact')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
