from django.http import request
from django.shortcuts import render,get_object_or_404
from .models import Gallery


# Create your views here.
def gallery(request):
    gallery = Gallery.objects.all()
    return render(request,'gallery/gallery.html',{'gallery':gallery})