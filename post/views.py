from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def api(request):
    if request.method == 'POST':        
        if(request.data):
            tags = request.data['tags'].split(',')
            
            post_write = Post()
            post_write.category = request.data['category'].lower()
            post_write.title = request.data['title']
            post_write.slug = request.data['slug']
            post_write.content = request.data['content']
            post_write.summary = request.data['summary']
            post_write.save()
            
            for tag in tags:
                post_write.tags.add(tag.replace("'", "").strip())
                
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        return redirect('/')
      

def index(request):
    categorys = ['HEALTH', 'COOKING', 'CAREER', 'PARENTING', 'SHOPPING']
    best_posts = Post.objects.order_by('-hits')[:3]
    health_posts1 = Post.objects.filter(category='health').order_by('-create_date')[:3]
    health_posts2 = Post.objects.filter(category='health').order_by('-create_date')[3:5]
    cooking_posts1 = Post.objects.filter(category='cooking').order_by('-create_date')[:3]
    cooking_posts2 = Post.objects.filter(category='cooking').order_by('-create_date')[3:5]
    career_posts1 = Post.objects.filter(category='career').order_by('-create_date')[:3]
    career_posts2 = Post.objects.filter(category='career').order_by('-create_date')[3:5]
    parenting_posts1 = Post.objects.filter(category='parenting').order_by('-create_date')[:3]
    parenting_posts2 = Post.objects.filter(category='parenting').order_by('-create_date')[3:5]
    shopping_posts1 = Post.objects.filter(category='shopping').order_by('-create_date')[:3]
    shopping_posts2 = Post.objects.filter(category='shopping').order_by('-create_date')[3:5]
    
    return render(request, 'index.html', {'best_posts': best_posts, 
                                          'health_posts1': health_posts1, 'health_posts2': health_posts2, 'health_category': categorys[0], 
                                          'cooking_posts1': cooking_posts1, 'cooking_posts2': cooking_posts2, 'cooking_category': categorys[1], 
                                          'career_posts1': career_posts1, 'career_posts2': career_posts2, 'career_category': categorys[2], 
                                          'parenting_posts1': parenting_posts1, 'parenting_posts2': parenting_posts2, 'parenting_category': categorys[3], 
                                          'shopping_posts1': shopping_posts1, 'shopping_posts2': shopping_posts2, 'shopping_category': categorys[4], 
                                          })

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.hits += 1
    post.save()
    
    posts = Post.objects.filter(category=post.category).exclude(id=post.id).order_by('-create_date')[:3]

    return render(request, 'post.html', {'post': post, 'posts': posts})
  