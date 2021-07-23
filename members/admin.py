from django.contrib import admin
from .models import Member , MemberImage

# Register your models here.
class MemberImageAdmin(admin.StackedInline):
    model = MemberImage
 
@admin.register(Member)
class MembertAdmin(admin.ModelAdmin):
    inlines = [MemberImageAdmin]
 
    class Meta:
       model = Member
 
#@admin.register(NewsImage)
class MemberImageAdmin(admin.ModelAdmin):
    pass
