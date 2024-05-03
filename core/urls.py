from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<str:quality>/book/<slug:slug>', views.BookDetailView.as_view(), name='book_detail'),
    path('<str:quality>/music/<slug:slug>', views.SongDetailView.as_view(), name='music_detail'),
    path('<str:quality>/video/<slug:slug>', views.VideoDetailView.as_view(), name='video_detail'),
    path('<str:quality>/podcast/<slug:slug>', views.PodcastDetailView.as_view(), name='podcast_detail'),
]