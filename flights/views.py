from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from flights.models import *

# Create your views here.

# def index(request):
#     return render(request, "flights/index.html", {
#         "flights": Flights.objects.all(),
#         "airports": Airport.departures.all(),
#     }) \

# def home_view(request,*args, **kwargs):
#     return HttpResponse("<h1>Hello World</h1>")

def index(request):
    airports = Airport.objects.all()  # This gets all airport instances
    flights = Flights.objects.all()  # This gets all flights instances
    return render(request, "flights/index.html", {
        "flights": flights,
        "airports": airports,
    })

def flight(request, flight_id):
    flight = Flights.objects.get(pk=flight_id)

    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "nonPassengers": passenger.objects.exclude(flights=flight).all(),
    })

def book(request, flight_id):
    if request.method == 'POST':
        flight = Flights.objects.get(pk=flight_id)
        passenger_name = passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger_name.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))
    