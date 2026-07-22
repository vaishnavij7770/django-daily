from django.shortcuts import render
from django.http import HttpResponse
from .models import register 

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
    return render(request, "register.html")


def formsave(request):
    if request.method=="POST":
        fn=request.POST["fullname"]
        em=request.POST["email"]
        cn=request.POST["contact"]
        ps=request.POST["password"]

        r = register(fullname=fn, email=em, contact=cn, password=ps)
        r.save()
        return HttpResponse("Registration saved")
    else:
        return HttpResponse("failed")