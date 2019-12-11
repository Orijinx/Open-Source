from django.conf.urls import url, include
from . import views
from feed.models import Articles
from django.views.generic import ListView, DetailView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/$', views.add_card, name='add_card'),
   # url(r'^/posts/post$',views.to_post, name = 'to_post'),\

]
