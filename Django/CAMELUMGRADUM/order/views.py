from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee_Bags




def Orders(request):
    coffee_bags = Coffee_Bags.objects.all()
    return render(request,"order/Orders.html", {'coffee_bags': coffee_bags})

