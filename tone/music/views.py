from django.views.generic.edit import FormView
from django.views import generic
from .models import Album, Song
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from music.forms import UserForm

class IndexView(generic.ListView):
	template_name = 'music/index.html'
	def get_queryset(self):
		return Album.objects.all()  
# this will return objects to template in a default variable called object_list
''' to override this default object_list create a context_object_name= 'hakka_noodle' and use this hakka_noodle in your template'''
class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'

#class DetailSong(generic.ListView):
#	template_name = 'music/song.html'
#	def get_queryset(self):
#		return Song.objects.all()
class AlbumCreate(CreateView):
	model = Album
	fields = ['artist', 'album_title', 'album_cover', 'genre']

class AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist', 'album_title', 'album_cover', 'genre']


class AlbumDelete(DeleteView):
	model = Album
	#fields = ['artist', 'album_title', 'album_cover', 'genre']
	success_url = reverse_lazy('music:index')

class UserformView(View):
	form_class = UserForm
	template_name = 'music/registration_form.html'
	
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form' : form})	
	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save(commit = False)
			#clean and normalized data - data that is formatted properly
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			# returns User objects if credentials are correct
			user = authenticate(username = username, password = password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('music:index')
		return render(request, self.template_name, {'form': form})
