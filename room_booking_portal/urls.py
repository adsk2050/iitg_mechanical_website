from django.urls import path, include, re_path
from .views import *

# app_name = "room_booking_portal"

urlpatterns = [
    path("", home, name="home"),
    path("booking/", BookingViews.as_view(), name="booking-objects"),
]
