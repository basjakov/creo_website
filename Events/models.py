from django.db import models
from django.db.models.base import Model
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    LANGUAGE= (
        ("en", "en"),
        ("fr", "fr"),
        ("fr", "ru"),
    )
    title =  models.CharField(max_length=100)
    event_date =  models.DateTimeField(default=timezone.now)
    lang = models.CharField(max_length=9,
                  choices=LANGUAGE,default="en") 
    post = models.TextField()
    def __str__(self):
        return self.title
class EventImage(models.Model):
    post = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'eventsimages/')