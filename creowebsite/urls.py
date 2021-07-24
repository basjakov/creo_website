from os import name
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import home.views
import members.views
import Events.views
import OurSongs.views
import news.views
import Gallery.views

urlpatterns = [
    path('',home.views.homepage, name='homepage'),
    path('members/<str:language>',members.views.all_members, name='members'),
    path('member/<int:id>',members.views.member, name='member'),
    #events
    path('events/<str:language>',Events.views.all_events, name='events'),
    path('event/<int:id>',Events.views.event, name='event'),
    #our songs
    path('oursongs/',OurSongs.views.all_songs, name='oursongs'),
    path('song/<int:id>',OurSongs.views.song, name='song'),
    #news
    path('news/<str:language>',news.views.all_news,name='all_news'),
    path('news/post/<str:id>',news.views.news,name='news'),
    #gallery
    path('gallery/',Gallery.views.gallery,name='gallery'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

