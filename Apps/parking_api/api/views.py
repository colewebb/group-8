from rest_framework import generics, permissions
from .models import Event, Lot, Spot, Reservation
from .serializers import EventSerializer, LotSerializer, SpotSerializer, ReservationSerializer
from .serializers import UserSerializer
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly


# Create your views here.


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LotList(generics.ListCreateAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class SpotList(generics.ListCreateAPIView):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SpotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
