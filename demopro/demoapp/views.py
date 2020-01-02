from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.

def Home(request):

    return HttpResponse("<h1>hello</h1>")
