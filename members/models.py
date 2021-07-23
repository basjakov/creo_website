from django.db import models

# Create your models here.
class Member(models.Model):
    LANGUAGE= (
        ("en", "en"),
        ("fr", "fr"),
        ("fr", "ru"),
    )
    name = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/members/')
    role = models.CharField(blank=True, null=True,max_length=150)
    lang = models.CharField(max_length=9,
                  choices=LANGUAGE,default="en")    
    biograph = models.TextField()
    linkedin = models.CharField(blank=True, null=True,max_length=150)
    twitter = models.CharField(blank=True, null=True,max_length=150)
    facebook = models.CharField(blank=True, null=True,max_length=150)
    instagram  = models.CharField(blank=True, null=True,max_length=150)
    soundcloud = models.CharField(blank=True, null=True,max_length=150)

class MemberImage(models.Model):
    post = models.ForeignKey(Member, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'membersimages/')