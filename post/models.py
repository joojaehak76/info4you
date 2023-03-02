from django.db import models
from taggit.managers import TaggableManager

   
class Post(models.Model):
    category = models.CharField(max_length=30, verbose_name='카테고리', 
			choices = {
				('health', 'health'),
				('cooking', 'cooking'),
				('career', 'career'),
				('parenting', 'parenting'),
				('shopping', 'shopping'),
			})
    title = models.CharField(max_length=100, verbose_name='제목')
    slug = models.SlugField(max_length=150, unique=True, allow_unicode=True,  verbose_name='제목별칭')
    content = models.TextField(verbose_name='내용')
    summary = models.TextField(verbose_name='요약')
    hits = models.IntegerField(default=0, verbose_name='조회수')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='생성시간')
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title
      