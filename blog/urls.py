from django.contrib import admin
from django.urls import path, include
from post.views import index


urlpatterns = [
	path('admin/', admin.site.urls),
	path('', index),
	path('category/', include('category.urls')),
	path('tag/', include('tag.urls')),
	path('post/', include('post.urls')),
]
