from django.conf.urls import url, include
from django.views.generic import ListView, DetailView, FormView
from user_prof.models import Users
from .views import addPost



urlpatterns = [
   # url(r'^$',ListView.as_view(queryset=Users.objects.all(), template_name="users/accounts.html")),
    # url(r'^$', views.),
   # url(r'^signup$', signup, name='signup'),
    url(r'^$', addPost, name='addPost'),
]
