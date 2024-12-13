from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Flight, Passenger

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    passengers = flight.passengers.all()

    # Get passengers who are not on the flight
    non_passengers = Passenger.objects.exclude(flights=flight)

    # Debugging: Print non_passengers
    print(non_passengers)

    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers,
        "non_passengers": non_passengers
    })


def book(request, flight_id):
    # For a POST request, add a new flight
    if request.method == "POST":
        # Accessing the flight
        flight = Flight.objects.get(pk=flight_id)

        # Finding the passenger id from the submitted form data
        passenger_id = request.POST.get("passenger")

        if passenger_id:
            passenger = Passenger.objects.get(pk=passenger_id)
            flight.passengers.add(passenger)

            # Debugging output
            print(f"Passenger added: {passenger}")
            print(f"Flight passengers: {flight.passengers.all()}")

            # Redirect user to flight page
            return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
        else:
            print("No passenger selected")
    
    return render(request, "flights/flight.html", {
        "flight": flight,
    })
