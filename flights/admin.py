from django.contrib import admin
from .models import Flight, Airport, Passenger

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Passenger)