from django.http import HttpResponse
from .models import Album, Song
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login         #authentice takes a username and a password while login gives a user session ID
from django.http import Http404
from django.views.generic import View
'''album = Album.objects.all()
def index(request):
    try:
        album = Album.objects.all()  #album will be equal to the object(name of the album) with given ID
    except Album.DoesNotExist:
        raise Http404("Album doesn't exist")
    return render(request, 'TEST/index.html', {'all_album' : album})
def album_data(request, album_id):
    album_dat = get_object_or_404(Album, pk = album_id)'''
   #return render(request, 'test/detail.html', {'album_name': album_dat} )
from django.views import generic
from Test.models import Album
class IndexView(generic.ListView):
    template_name = "Test/index.html"
    context_object_name = "all_albums"
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'Test/detail.html'

def favorite(request, album_id):
    album = get_object_or_404(Album, pk = album_id)
    try:
        selected_song = album.song_set.get(pk = request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'Test/detail.html', {'album': album, 'error_message':" You did not select a valid song"})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'Test/detail.html', {'album': album})


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo', ]


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo', ]


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('Test:index')
'''class SongCreate(CreateView):
    model = Song
    fields = ['song_title',]'''


def AddSong(request, album_id):
    return render(request, 'Test/newsong.html', {'album': album_id})


def added(request, album_id):
    details = Song()
    album_dat = get_object_or_404(Album, pk=album_id)
    details.album = album_dat
    details.song_title = request.GET.get('song_name')
    details.save()
    return redirect('/login/test/' + str(album_id))
# album_title, genre            parameters
    #try:
        #album_name = Album.objects.get(pk = album_id)   #album will be equal to the object(name of the album) with given ID
    #except Album.DoesNotExist:
        #raise Http404("Album doesn't exist")
    #return render(request, 'test/detail.html', {'album' : album_name})


 

      #return HttpResponse("<h1>Album ID = "+ str(album_id) + "</h1>")
##def artist_data(request, name):
  #    ID = Album.objects.filter(artist__startswith = str(name))
       #   return HttpResponse("<h1> Artist name is " + (name) +" and its ID is " + str(ID[0].id) +" </h1>")



##          WITHOUT HTML IN PYTHON.
#def index(request):
      #html = ''
      #for name in iterate:
            #url = '/test/' + str(name.artist) + '/'
           #html += '<a href = "' + url + '">' + name.album_title + '</a><br>'
      #return HttpResponse(html)
      #html = ''
      #for var in iterate:
            #url = '/test/' + str(var.id) + '/'
            #html += '<h1><a href="' + url + '">' + var.album_title + '</ a>'
      #return HttpResponse(html)