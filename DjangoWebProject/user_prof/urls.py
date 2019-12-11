from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from user_prof.models import Users

urlpatterns = [
    # url(r'^$', 
    # ListView.as_view(queryset=Users.objects.all(),template_name="users/accounts.html")),
    url(r'^$', views.),


]