import requests

from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    req = requests.get("http://httpbin.org/status/418")
    print(req.text)
    return HttpResponse("<pre>{}</pre>".format(req.text))
    # return HttpResponse('Hello from Python!')
    #return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

