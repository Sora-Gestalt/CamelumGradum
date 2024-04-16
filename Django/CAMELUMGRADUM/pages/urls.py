# this urls is for the app and must be connected to the project urls
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Welcome, name='index'),
    path("about", views.about, name='index2'),
    path("Menu", views.Menu, name='index3'),
]

