from django.db.models import query
from django.db.models.expressions import F
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.http import JsonResponse
from rest_framework.serializers import Serializer
# from .forms import ArtistForm, SongForm
from .models import Artist, Song
from rest_framework import generics
from .serialzers import ArtistSerializer, SongSerializer
# # Create your views here.
# METHODS / HTTP VERBs
# REST Action "route" = Path + method
#
#list       artist/         GET
#create     artist/         POST
#detail     artist/<id>     Get
#update     artist/<id>     PATCH
#destroy    artist/<id>     DESTROY

def hotsongs(request):
    JsonResponse(list(Song.objects.all().values()),safe=False),

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


# def demo_json(request):
#     data = {'a:1','b:2'}
#     return JsonResponse(data)

# def sample_mv(request):
#     output = Artist.objects.all()
#     print(output)
#     JsonResponse(output)    

# def artist_list(request):
#     artists = Artist.objects.all()
#     return render(request, 'tunr/artist_list.html', {'artists': artists})

# def artist_detail(request, pk):
#     artist = Artist.objects.get(id=pk)
#     return render(request, 'tunr/artist_detail.html', {'artist': artist})

# def artist_create(request):
#     if request.method == 'POST':
#         form = ArtistForm(request.POST)
#         if form.is_valid():
#             artist = form.save()
#             return redirect('artist_detail', pk=artist.pk)
#     else:
#         form = ArtistForm()
#     return render(request, 'tunr/artist_form.html', {'form': form})

# def artist_edit(request, pk):
#     artist = Artist.objects.get(pk=pk)
#     if request.method == "POST":
#         form = ArtistForm(request.POST, instance=artist)
#         if form.is_valid():
#             artist = form.save()
#             return redirect('artist_detail', pk=artist.pk)
#     else:
#         form = ArtistForm(instance=artist)
#     return render(request, 'tunr/artist_form.html', {'form': form})

# def artist_delete(request, pk):
#     Artist.objects.get(id=pk).delete()
#     return redirect('artist_list')

# def song_list(request):
#     songs = Song.objects.all()
#     return render(request, 'tunr/song_list.html', {'songs': songs})

# def song_detail(request, pk):
#     song = Song.objects.get(id=pk)
#     return render(request, 'tunr/song_detail.html', {'song': song})

# def song_create(request):
#     if request.method == 'POST':
#         form = SongForm(request.POST)
#         if form.is_valid():
#             song = form.save()
#             return redirect('song_detail', pk=song.pk)
#     else:
#         form = SongForm()
#     return render(request, 'tunr/song_form.html', {'form': form})

# def song_edit(request, pk):
#     song = Song.objects.get(pk=pk)
#     if request.method == "POST":
#         form = SongForm(request.POST, instance=song)
#         if form.is_valid():
#             song= form.save()
#             return redirect('song_detail', pk=song.pk)
#     else:
#         form =SongForm(instance=song)
#     return render(request, 'tunr/song_form.html', {'form': form})

# def song_delete(request, pk):
#     Song.objects.get(id=pk).delete()
#     return redirect('song_list')