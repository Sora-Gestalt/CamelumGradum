from django.urls import path
from . import views

urlpatterns = [
    path("", views.Reservation, name="Reservation"),
]