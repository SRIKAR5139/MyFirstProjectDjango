from django.shortcuts import render
from django.http import HttpResponse

#myname="Srikar"

def home(request):
    return HttpResponse("Hello world")
