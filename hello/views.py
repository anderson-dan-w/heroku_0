from __future__ import print_function
import requests

from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    return HttpResponse("Hello")
    #req = requests.get("http://httpbin.org/status/418")
    #print(req.text)
    #return HttpResponse("<pre>{}</pre>".format(req.text))


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

