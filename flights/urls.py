from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # URL path for the index view
    path("<int:flight_id>", views.flight, name="flight"),  # URL path for the flight detail view
]