from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    message =  Post.objects.get(id = 1)
    messages =  message.body
    return HttpResponse(messages)


def database_view(request):
    post = Post.objects.get(id = 1)
    poster = Post.objects.get(id = 1)
    message = post.summary
    title = poster.title
    return HttpResponse(message, title)
