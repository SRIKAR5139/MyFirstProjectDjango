from django.shortcuts import render
from django.http import HttpResponse

myname="Srikar"

def home(request):
    return render(request,'home.HTML',{'name':myname})


def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    val3=val1+val2
    return render(request,'result.HTML',{'result':val3})

def dashboard(request):
    return render(request,'dashboard.HTML')
    
    #HttpResponse("Hello world")
    