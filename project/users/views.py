from django.shortcuts import render
from django.contrib import auth
from main.models import Post

# Create your views here.
def mypage(request):
    if request.user.is_authenticated:
        posts=Post.objects.filter(writer =request.user.username)
    return render(request, 'users/mypage.html', {'posts': posts})