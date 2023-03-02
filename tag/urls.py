from django.urls import path
from . import views


urlpatterns = [
    path('<str:tag>', views.tag, name='tag'),
]
