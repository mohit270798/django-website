from django.http import HttpResponse
from django.shortcuts import render

from .models import Album

# Create your views here.


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/albums.html', context)


def detail(request, id):
    return HttpResponse('You are viewing album no.' + str(id))
