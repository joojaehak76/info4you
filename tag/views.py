from django.shortcuts import render
from post.models import Post
from taggit.models import Tag


def tag(request, tag):
    posts1 = Post.objects.filter(tags__name__in=[tag]).order_by('-create_date')[:5]
    posts2 = Post.objects.filter(tags__name__in=[tag]).order_by('-create_date')[5:3]
    
    tags = Tag.objects.all()[:10]
    
    return render(request, 'tag.html', {'tag': tag, 'posts1': posts1, 'posts2': posts2, 'tags': tags})
