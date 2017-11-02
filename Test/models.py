from django.db import models
from django.core.urlresolvers import reverse
class Album(models.Model):
    artist = models.CharField(max_length = 50, null = True)
    album_title = models.CharField(max_length = 100, null = True)
    genre = models.CharField(max_length = 100, null = True)
    album_logo = models.FileField(max_length = 1000, null = True)
    def get_absolute_url(self):
        return reverse('Test:album_data', kwargs = {'pk': self.pk})
    def __str__(self):
        return  self.album_title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE, null = True)
    song_title = models.CharField(max_length = 100, null = True)
    is_favorite = models.BooleanField(default = False)
    def get_absolute_url(self):
        return reverse('Test:album_data', kwargs = {'pk': self.album.pk})
    def __str__(self):
        return self.song_title
