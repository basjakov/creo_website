from django.db import models
from django.shortcuts import render, get_object_or_404
from .models import Event,EventImage

# Create your views here.
def all_events(request,language):
    events = Event.objects.filter(lang=language)
    return render(request,'events/events.html',{'events':events})
def event(request,id):
    event= get_object_or_404(Event,pk=id)
    EventImages = EventImage.objects.filter(post_id=id)
    return render(request,'events/event.html',{'event':event,'EventImages':EventImages})