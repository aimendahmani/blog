from unicodedata import name
from django.urls import URLPattern
from django.views import View

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index' ),
    path('post/<str:pk>', views.Post, name='Post')
]