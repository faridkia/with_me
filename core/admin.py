from django.contrib import admin
from .models import *


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['feeling', 'name', 'author']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ['feeling', 'name']
    list_filter = ['created_at']
    search_fields = ['name']

@admin.register(Score_User)
class Score_UserAdmin(admin.ModelAdmin):
    list_display = ['score', 'user']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['feeling', 'name']
    list_filter = ['created_at']
    search_fields = ['name']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['feeling', 'name', 'singer']
    list_filter = ['created_at']
    search_fields = ['name']

@admin.register(PodcastComment)
class PodcastCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'podcast', 'is_published','reply']
    list_editable = ['is_published']
    list_filter = ['created_at']
    search_fields = ['name']

@admin.register(SongComment)
class SongAdmin(admin.ModelAdmin):
    list_display = ['user', 'song', 'is_published', 'reply']
    list_editable = ['is_published']
    list_filter = ['created_at']
    search_fields = ['name']

@admin.register(Feeling)
class FeelingAdmin(admin.ModelAdmin):
    list_display = ['quality']