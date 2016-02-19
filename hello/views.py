from __future__ import print_function
import os
import sys

from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

THIS_DIR = os.path.dirname(__file__)

def dprint(*args, **kwargs):
    print(*args, **kwargs)
    sys.stdout.flush()

def blogParse(fname):
    if not os.path.exists(fname):
        return {}
    d = {}
    with open(fname) as fh:
        lines = fh.read().split("\n")
    toRemove = {l for l in lines if l.startswith("#")}
    for line in toRemove:
        lines.remove(line)
        if line.startswith("#title"):
            d['title'] = line.replace("#title ","")
        elif line.startswith("#tags"):
            d['tags'] = line.split()[1:] ## skip '#tags'
        elif line.startswith("#published"):
            d['published'] = line.replace("#published ","")
        elif line.startswith("#lastEdit"):
            d['lastEdit'] = line.replace("#lastEdit ","")
    d['text'] = "\n".join(lines)
    return d

# Create your views here.
def index(request):
    return render(request, 'index.html')

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})

def blogs(request):
    return render(request, "blogs.html")

def nblog(request, blogIndex=-1):
    ctx = dict(blogIndex=blogIndex, text="empty text")
    fname = os.path.join(THIS_DIR, "blogs", "{}.txt".format(blogIndex))
    ctx.update(blogParse(fname))
    return render(request, "blogs.html", ctx)

