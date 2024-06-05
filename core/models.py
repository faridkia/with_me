from django.db import models
from accounts.models import User
from django.utils.text import slugify
class Feeling(models.Model):
    CHOICES = (
        ('khosh', 'خوشحال'),
        ('khoob', 'خوب'),
        ('na', 'ناراحت'),
        ('asab', 'عصبانی'),
    )
    quality = models.CharField(choices=CHOICES, max_length=10, unique=True)

    def __str__(self):
        return f'{self.quality}'

class Book(models.Model):
    feeling = models.ForeignKey(Feeling, on_delete=models.PROTECT, related_name='books')
    image = models.ImageField(upload_to='books/images/', verbose_name='عکس')
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=1000)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['-created_at']
class Podcast(models.Model):
    feeling = models.ForeignKey(Feeling, on_delete=models.PROTECT, related_name='podcast')
    audio = models.FileField(upload_to='audios/audios/')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='audios/images/')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return f'{self.name}'
    class Meta:
        ordering = ['-created_at']

class Score_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='podcast_scores')
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='scores')
    score = models.PositiveSmallIntegerField()

class PodcastComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد شده')
    text = models.CharField(max_length=300, verbose_name='متن')
    reply = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True, blank=True, verbose_name='ریپلای')
    is_published = models.BooleanField(default=False, verbose_name='منتشر')

    def __str__(self):
        return f"{self.user.username}{self.id}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت پادکست ها'

class SongComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,verbose_name='کاربر')
    song = models.ForeignKey('Song', on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد شده')
    text = models.CharField(max_length=300, verbose_name='متن')
    reply = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True, blank=True, verbose_name='ریپلای')
    is_published = models.BooleanField(default=False, verbose_name='منتشر')

    def __str__(self):
        return f"{self.user.username}{self.id}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت اهنگ ها'


class Video(models.Model):
    feeling = models.ForeignKey(Feeling, on_delete=models.PROTECT, related_name='videos')
    image = models.ImageField(upload_to='videos/images/')
    video = models.FileField(upload_to='videos/')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['-created_at']


class Song(models.Model):
    feeling = models.ForeignKey(Feeling, on_delete=models.PROTECT, related_name='podcasts')
    name = models.CharField(max_length=50)
    audio = models.FileField(upload_to='songs/audios/')
    image = models.ImageField(upload_to='songs/images/')
    singer = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['-created_at']
