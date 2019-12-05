from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello</h1><style type='text/css'>h1{color: red;justify-content: center;font-size: 2em}</style>")
# Create your views here.
