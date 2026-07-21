from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("Im Home page")
    return render(request,"home.html")

def about(request):
    # return HttpResponse("Im about page")
    return render(request,"about.html")

def contact(request):
    return HttpResponse("contact us")

def register(request):
    return HttpResponse("register.html")