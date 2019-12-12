from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from feed.models import Articles

urlpatterns = [
    url(r'^$', 
    ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:10],template_name="feed/posts.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Articles, template_name = "feed/post_pg.html"))
]
