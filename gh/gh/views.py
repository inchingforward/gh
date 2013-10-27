from django.shortcuts import render
from posts.models import Post


def index(request):
    posts = Post.objects.all().order_by('-created')[0:30]
    
    return render(request, 'index.html', {'posts': posts})