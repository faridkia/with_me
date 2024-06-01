from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<str:quality>/book/<int:id>', views.BookDetailView.as_view(), name='book_detail'),
    path('<str:quality>/music/<int:id>', views.SongDetailView.as_view(), name='music_detail'),
    path('<str:quality>/video/<int:id>', views.VideoDetailView.as_view(), name='video_detail'),
    path('<str:quality>/podcast/<int:id>', views.PodcastDetailView.as_view(), name='podcast_detail'),
    path('about-us', views.AboutUsView.as_view(), name='about_us'),
]