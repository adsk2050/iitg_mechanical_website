from rest_framework import serializers
from .models import Booking, RoomForBookingPortal
from mechweb.models import CustomUser
from django.core.exceptions import ValidationError
from django.db.models import Q


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email",)


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomForBookingPortal
        fields = ("title", "available")


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "id",
            "user",
            "room",
            "title",
            "reason",
            "startTime",
            "endTime",
        ]

    def to_representation(self, instance):
        rep = super(BookingSerializer, self).to_representation(instance)
        rep["user"] = {"name": instance.user.get_full_name(), "email": instance.user.email}
        rep["room"] = instance.room.title
        return rep


class BookingWriteSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer

    def validate(self, data):

        start = data["startTime"]
        end = data["endTime"]
        room = data["room"]
        if start >= end:
            raise ValidationError("StartTime should be before endTime")

        bookingConflict = Booking.objects.filter(Q(room=room), ~Q(Q(startTime__gte=end) | Q(endTime__lte=start))).exists()
        if bookingConflict:
            raise ValidationError("Booking timing for " + room.title + " is conflicting with other bookings.")
        return data

    class Meta:
        model = Booking
        fields = [
            "id",
            "user",
            "room",
            "title",
            "reason",
            "startTime",
            "endTime",
        ]
