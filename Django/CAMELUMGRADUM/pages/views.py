from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Welcome(request):
    x = {"name": "nawaf abdullah al taleb"}
    return render(request, "pages/Welcome.html", x)

def about(request):
    return render(request, "pages/about.html")


def Menu(request):
    return render(request, "pages/Menu.html")

