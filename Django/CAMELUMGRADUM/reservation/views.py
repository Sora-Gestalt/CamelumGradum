from django.shortcuts import render
from django.http import HttpResponse
from .forms import ReserveForm
from .models import Reserve
from django.shortcuts import redirect

def Reservation(request):
    context = {}
    form = ReserveForm()
    Reserves = Reserve.objects.all()
    if request.method == "POST":
        if "submit" in request.POST:
            form = ReserveForm(request.POST)
            form.save()
    context["form"] = form
    return render(request,  "reservation/Reservation.html",context )
