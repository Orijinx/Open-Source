from django.shortcuts import render
from .forms import add_post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from feed.models import Articles
import datetime
import geocoder
import urllib
from yandex_geocoder import Client


def addPost(request):
    form = add_post(request.POST or None)
    if form.is_valid():

        img = form.cleaned_data.get("img_url")
        tit = form.cleaned_data.get("title")
        abo = form.cleaned_data.get("about")
        tag = form.cleaned_data.get("tag")


        g = geocoder.ip('me')
       # print(Client.coordinates('55.0968, 36.6101'))
        print(g.latlng)
        print(g[0])
        try:
            s = Articles(img_url=img,
                         title=tit,
                         about=abo,
                         tag=tag,
                         date=datetime.datetime.now(),
                         location=g[1]
                         )
            s.save()
            context = {'form': form}
        except Exception:
            context = {'form': form, 'error':'Ethernet error'}

        
        return render(request, 'users/accounts.html', context)

    # user= authe,nticate(username=uservalue, password=passwordvalue)
    # if user is not None:
    #     login(request, user)
    #     context= {'form': form,
    #               'error': 'The login has been successful'}

    #     return render(request, 'includes/index.html', context)
    # else:
    #     context= {'form': form,
    #               'error': 'The username and password combination is incorrect'}

    #     return render(request, 'users/accounts.html', context )

    else:
        context = {'form': form}
        return render(request, 'users/accounts.html', context)
