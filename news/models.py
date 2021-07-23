from django.db import models
from django.utils import timezone

# Create your models here.

class News(models.Model):
    LANGUAGE= (
        ("en", "en"),
        ("fr", "fr"),
        ("fr", "ru"),
    )

    
    title = models.CharField(max_length=100)    
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/news/')
    lang = models.CharField(max_length=9,
                  choices=LANGUAGE,default="en") 
    post = models.TextField()
    meta_description = models.CharField(max_length=200,default="")
    meta_keywords = models.CharField(max_length=200,default="")

    def __str__(self):
        return self.title
class NewsImage(models.Model):
    post = models.ForeignKey(News, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'newsimages/')
    