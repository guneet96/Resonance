from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Album(models.Model):
	album_title = models.CharField(max_length = 250)
	album_cover = models.CharField(max_length = 250)
	genre = models.CharField(max_length = 250)
	desc = models.CharField(max_length = 600, blank = True)
	def get_absolute_url(self):
 		return reverse('music:detail', kwargs={'pk': self.pk})

	def __str__(self):
		return self.album_title

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE)
	genre = models.CharField(max_length = 20)
	song_title = models.CharField(max_length = 100)
	e_link = models.URLField(blank = True)
	def __str__(self):
		return self.song_title
