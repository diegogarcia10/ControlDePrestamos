import requests
from django.shortcuts import render
from django.http import HttpResponse

#Agregados para hacer CRUD
from django.views.generic import ListView

# Create your views here.

def index(request):
    # return HttpResponse('Hello from Python!')
    #return render(request, 'index.html')
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')