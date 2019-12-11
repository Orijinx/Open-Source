from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic import View
from django.contrib import messages
from feed.models import Articles
from .forms import PostForm


class SomePost(View):
      def post(self, request):
        form = PostForm(request.POST)
        db = form.save()
        c = {'form':form}
        return render(request,'user_form.html', c )
