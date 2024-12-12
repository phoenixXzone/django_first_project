from django.shortcuts import render, get_object_or_404
from .models import Flight

def index(request):
    flights = Flight.objects.all()
    return render(request, "flights/index.html", {
        "flights": flights
    })

def flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight
    })