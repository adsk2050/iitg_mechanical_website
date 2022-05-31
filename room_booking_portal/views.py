from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Booking, RoomForBookingPortal
from .serializers import BookingSerializer, BookingWriteSerializer
import json
from rest_framework.views import APIView


class BookingViews(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                booking = Booking.objects.get(pk=pk)
                serializer = BookingSerializer(booking)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookingWriteSerializer(data=request.data)
        isValid = serializer.is_valid()
        if not isValid:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        isAuthorized = request.user.is_superuser or (
            request.user.is_authenticated and request.user.groups.filter(name="Faculty").exists() and serializer.validated_data["user"] == request.user
        )
        if not isAuthorized:
            return Response({"status": "error", "data": {"error": "Not authorized"}}, status=status.HTTP_401_UNAUTHORIZED)

        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        try:
            booking = Booking.objects.get(pk=pk)
            if request.user.is_superuser or request.user == booking.user:
                booking.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

            return Response(status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


def home(request):
    # only superusers and faculties can edit
    canEdit = request.user.is_superuser or (request.user.is_authenticated and request.user.groups.filter(name="Faculty").exists())
    rooms = list(RoomForBookingPortal.objects.all().values())
    context = {
        "canEdit": canEdit,
        "rooms": rooms,
        "roomsStr": json.dumps(rooms),
    }
    return render(request, "room_booking_portal/room_booking_portal.html", context)
