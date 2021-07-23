from django.db import models
from django.db.models.base import Model

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to = "gallery/")
