from django.shortcuts import render
from post.models import Post
from taggit.models import Tag


def category(request, category):
    posts1 = Post.objects.filter(category=category).order_by('-create_date')[:5]
    posts2 = Post.objects.filter(category=category).order_by('-create_date')[5:3]
    
    categorys = ['health', 'cooking', 'career', 'parenting', 'shopping']
    categorys.remove(category)
    
    tags = Tag.objects.all()[:10]
    
    return render(request, 'category.html', {'category': category, 'categorys': categorys,
                                             'posts1': posts1, 'posts2': posts2, 
                                             'tags': tags,
                                             })
