from django.shortcuts import render, redirect
from django.views.generic import View
# TODO : book detail, song detail, podcast detail, video detail, templates
from django.shortcuts import get_object_or_404
from accounts.models import User
from .models import *

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user.username)
        else:
            user = None
        return render(request, '', {'user' : user})
class BookDetailView(View):
    def get(self, request, quality, id):
        feeling = get_object_or_404(Feeling, quality=quality)
        book = Book.objects.filter(feeling=feeling, id=id)
        return render(request, '', {'book' : book})

class SongDetailView(View):
    def get(self, request, quality, id):
        feeling = get_object_or_404(Feeling, quality=quality)
        song = Song.objects.filter(feeling=feeling, id=id)
        return render(request, '', {'song': song})

class PodcastDetailView(View):
    def get(self, request, quality, id):
        feeling = get_object_or_404(Feeling, quality=quality)
        podcast = Book.objects.filter(feeling=feeling, id=id)
        return render(request, '', {'podcast': podcast})

class VideoDetailView(View):
    def get(self, request, quality, id):
        feeling = get_object_or_404(Feeling, quality=quality)
        video = Book.objects.filter(feeling=feeling, id=id)
        return render(request, '', {'video': video})

