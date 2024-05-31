from django.shortcuts import render, redirect
from django.views.generic import View
# TODO : all templates, navbar, footer margin down, links ,Debug, data
from django.shortcuts import get_object_or_404
from accounts.models import User
from .models import *

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user.username)
        else:
            user = None
        khosh = Feeling.objects.get(quality='khosh')
        khoob = Feeling.objects.get(quality='khoob')
        na = Feeling.objects.get(quality='na')
        asab = Feeling.objects.get(quality='asab')
        return render(request, 'core/home.html', {'user' : user, 'khosh':khosh, 'khoob':khoob, 'na':na, 'asab':asab})
class BookDetailView(View):
    def get(self, request, quality, id):
        feeling = get_object_or_404(Feeling, quality=quality)
        book = get_object_or_404(Book, feeling=feeling, id=id)
        books = Book.objects.all()[0:3]
        return render(request, 'core/book.html', {'book' : book, 'books': books})

class SongDetailView(View):
    def get(self, request, quality, id):
        feeling = get_object_or_404(Feeling, quality=quality)
        song = get_object_or_404(Song, feeling=feeling, id=id)
        songs = Song.objects.all()[0:3]
        return render(request, 'core/song.html', {'song': song, 'songs':songs})

class PodcastDetailView(View):
    def get(self, request, quality, id):
        feeling = get_object_or_404(Feeling, quality=quality)
        podcast = get_object_or_404(Podcast, feeling=feeling, id=id)
        podcasts = Podcast.objects.all()[0:3]
        return render(request, 'core/podcast.html', {'podcast': podcast, 'podcasts':podcasts})

class VideoDetailView(View):
    def get(self, request, quality, id):
        feeling = get_object_or_404(Feeling, quality=quality)
        video = get_object_or_404(Video, feeling=feeling, id=id)
        videos = Video.objects.all()[0:3]
        return render(request, 'core/video.html', {'video': video, 'videos':videos})

