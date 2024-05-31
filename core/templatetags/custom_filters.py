import random
from django import template
from ..models import *
register = template.Library()

@register.simple_tag
def book_random_number(feeling:1):
    arr = []
    feeling1 = Feeling.objects.get(id=feeling)
    count = Book.objects.filter(feeling=feeling1)
    for i in count:
        arr.append(i.id)
    res = random.choices(arr)
    for i in res:
        count = i
    return count

@register.simple_tag
def podcast_random_number(feeling:1):
    arr = []
    feeling1 = Feeling.objects.get(id=feeling)
    count = Podcast.objects.filter(feeling=feeling1)
    for i in count:
        arr.append(i.id)
    res = random.choices(arr)
    for i in res:
        count = i
    return count

@register.simple_tag
def video_random_number(feeling):
    arr = []
    feeling1 = Feeling.objects.get(id=feeling)
    count = Video.objects.filter(feeling=feeling1)
    for i in count:
        arr.append(i.id)
    res = random.choices(arr)
    for i in res:
        count = i
    return count
@register.simple_tag
def song_random_number(feeling:1):
    arr = []
    feeling1 = Feeling.objects.get(id=feeling)
    count = Song.objects.filter(feeling=feeling1)
    for i in count:
        arr.append(i.id)
    res = random.choices(arr)
    for i in res:
        count = i
    return count
