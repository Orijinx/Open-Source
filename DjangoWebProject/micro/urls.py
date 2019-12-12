from django.conf.urls import url, include
from django.views.generic import ListView, DetailView, FormView
from user_prof.models import Users
from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import qr_serv


urlpatterns = [
    url(r'^$', views.micro, name="micro"),
    url(r'^qr$', qr_serv, name='qr_serv'),
]
