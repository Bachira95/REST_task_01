from datetime import datetime
from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import FlightsListSerializer, BookingListSerializer



class FlightsList(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightsListSerializer


class BookingList(ListAPIView):
    queryset = Booking.objects.filter(date__gt=datetime.today())
    serializer_class = BookingListSerializer
