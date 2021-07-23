from django.db import models
from django.utils import timezone

# Create your models here.
class OurSong(models.Model):
    song_name = models.CharField(max_length=150)
    title = models.CharField(max_length=500)
    date_time = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='songs/')
    song = models.FileField(upload_to='songs/')