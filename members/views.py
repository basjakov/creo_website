from django.shortcuts import render, get_object_or_404

from .models import Member,MemberImage


# Create your views here.
def all_members(request,language):
    members = Member.objects.filter(lang=language)
    return render(request,'members/members.html',{'members':members})
def member(request,id):
    member= get_object_or_404(Member,pk=id)
    MemberImages = MemberImage.objects.filter(post_id=id)
    return render(request,'members/member.html',{'member':member,'MemberImages':MemberImages})