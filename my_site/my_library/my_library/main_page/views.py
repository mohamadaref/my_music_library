import requests
from main_page.models import *
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from . import models
from . import urls
from my_library.urls import *
from django.shortcuts import get_object_or_404

def main_page(request):
    songs_list = Music.objects.order_by('music_name')
    album_list = Album.objects.order_by('album_name')
    context = {'songs_list' : songs_list, 'album_list' : album_list}
    return render(request,'main_page/index.html',context)

def download(request, song_name):
    song = Music.objects.get(music_name = str(song_name))
    r = requests.get(song.download_link, allow_redirects=True)
    open("/home/mohamad-aref/my_projects/my_site/my_library/my_library/downloads/" + str(song_name) + '.mp3', 'wb').write(r.content)
    context = {'song_info' : song}
    return render(request,'main_page/song_information.html',context)


def downloadal(request, song_name, alb_name):
    songs = Album.objects.get(album_name = str(alb_name))
    special_song = songs.music_set.get(music_name = str (song_name))
    r = requests.get(special_song.download_link, allow_redirects=True)
    open("/home/mohamad-aref/my_projects/my_site/my_library/my_library/downloads/" + str(song_name) + '__' + str(alb_name) +'.mp3', 'wb').write(r.content)
    context = {'song_info' : special_song}
    return render(request,'main_page/song_information.html',context)


def downloadmu(request, song_name, alb_name, musician_name):
    musicians = Musician.objects.get(first_name = str(musician_name))
    albums = musicians.album_set.get(album_name = str(alb_name))
    special_song = albums.music_set.get(music_name = str(song_name))
    r = requests.get(special_song.download_link, allow_redirects=True)
    open("/home/mohamad-aref/my_projects/my_site/my_library/my_library/downloads/" + str(song_name) +'__'+ str(alb_name) + '__' + str(musician_name) +'.mp3', 'wb').write(r.content)
    return HttpResponse(special_song.download_link)


def alb_detail(request, alb_name):
    songs = Album.objects.get(album_name = str(alb_name))
    songs_list_of_album = songs.music_set.all()
    context = {'songs' : songs , 'songs_list_of_album' : songs_list_of_album}
    return render(request,'main_page/album_information.html',context)

def musician_detail(request, musician_name):
    special_musician = Musician.objects.get(first_name = str(musician_name))
    return HttpResponseRedirect(reverse('musician_det',args=(songs.musician,)))
# Create your views here.
