from __future__ import print_function
import os
import sys

from django.shortcuts import render

from .models import Greeting
from . import blog_parser

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


def bookclub(request):
    return render(request, 'bookclub.html')


def blogs(request):
    ctx = {}
    ctx["recentSnippets"] = blog_parser.getRecentSnippets()
    return render(request, "blogs.html", ctx)


def nblog(request, blogIndex=-1):
    ctx = dict(blogIndex=blogIndex, text="empty text")
    fname = os.path.join(THIS_DIR, "blogs", "{}.txt".format(blogIndex))
    ctx.update(blog_parser.parseBlog(fname))
    return render(request, "blogs.html", ctx)

