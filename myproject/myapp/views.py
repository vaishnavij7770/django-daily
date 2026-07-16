from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Im Home page")

def about(request):
    return HttpResponse("Im about page")

def contact(request):
    return HttpResponse("contact us")