from django.shortcuts import render

from .models import Post

def post_list(request):
    post = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts: posts'})# Create your views here.
