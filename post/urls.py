from django.urls import path
from . import views


urlpatterns = [
    path('api', views.api, name='api'),
    path('<slug>', views.post, name='post'),
]
