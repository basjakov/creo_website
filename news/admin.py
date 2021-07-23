from django.contrib import admin
from .models import News , NewsImage

# Register your models here.
class NewsImageAdmin(admin.StackedInline):
    model = NewsImage
 
@admin.register(News)
class PostAdmin(admin.ModelAdmin):
    inlines = [NewsImageAdmin]
 
    class Meta:
       model = News
 
#@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    pass
