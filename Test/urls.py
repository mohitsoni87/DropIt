from django.conf.urls import url, include
from . import views
app_name = 'Test'
urlpatterns = [url(r'^$', views.IndexView.as_view(), name ='index'),
               #url(r'(?P<name>[A-Za-z]*)/$', views.artist_data, name = 'artist_data'),
               url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'album_data'),
               url(r'^username', include('User.urls')),
               url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite, name = 'favorite'),


               #Test/album/add      No need of primary key
               url(r'^album/add/$', views.AlbumCreate.as_view(), name = 'album-add'),

               #Test/album/2
               url(r'^album/(?P<pk>[0-9]+)/update', views.AlbumUpdate.as_view(), name = 'album-update'),

               #Test/album/2/delete

               url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name = 'album-delete'),

               #url(r'^add-song/(?P<pk>[0-9]+)$', views.SongCreate.as_view(), name = 'add-song')
                url(r'^(?P<album_id>[0-9]+)/newsong/', views.AddSong, name = 'add-song'),
                url(r'^(?P<album_id>[0-9]+)/edit/$', views.added, name = 'added'),
               ]


               #url(r'^albums', views.added, name = 'added'),'''
 
