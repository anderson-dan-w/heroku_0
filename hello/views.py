from __future__ import print_function
import os
import sys

from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import blogParser

THIS_DIR = os.path.dirname(__file__)

def dprint(*args, **kwargs):
    print(*args, **kwargs)
    sys.stdout.flush()

def index(request):
    return render(request, 'index.html')

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})

def aboutme(request):
    return render(request, 'aboutme.html')

def books(request):
    return render(request, 'books.html')

def blogs(request):
    ctx = {}
    ctx["recentSnippets"] = blogParser.getRecentSnippets()
    return render(request, "blogs.html", ctx)

def nblog(request, blogIndex=-1):
    ctx = dict(blogIndex=blogIndex, text="empty text")
    fname = os.path.join(THIS_DIR, "blogs", "{}.txt".format(blogIndex))
    ctx.update(blogParser.parseBlog(fname))
    return render(request, "blogs.html", ctx)

