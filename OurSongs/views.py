from django.http import request
from django.shortcuts import render,get_object_or_404

from .models import OurSong


# Create your views here.
def all_songs(request):
    all_songs = OurSong.objects.all()
    return render(request,'oursongs/allsongs.html',{'all_songs':all_songs})    
def song(request,id):
    song = get_object_or_404(OurSong,pk=id)
    return render(request,'oursongs/song.html',{'song':song})


