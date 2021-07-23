from django.http import request
from django.shortcuts import render,get_object_or_404
from .models import News,NewsImage

# Create your views here.
def all_news(request,language):
    news = News.objects.filter(lang=language)
    return render(request,'news/all_news.html',{'all_news':news})
def news(request,id):
    news = get_object_or_404(News,pk=id)    
    news_images = NewsImage.objects.filter(post_id=id)
    return render(request,'news/news.html',{'news':news,'news_images':news_images})