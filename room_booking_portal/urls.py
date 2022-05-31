from django.urls import path, include, re_path
from .views import *

app_name = "room_booking_portal"

urlpatterns = [
    path("", home, name="room_booking_portal"),
    path("booking/", BookingViews.as_view(), name="booking-objects"),
    path("booking/<int:pk>/", BookingViews.as_view(), name="booking-objects"),
]
