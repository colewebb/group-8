from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Event, Lot, ParentLot, Reservation, Balance
from .serializers import EventSerializer, LotSerializer, PLotSerializer, ReservationSerializer
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly, IsSuperUserOrReadOnly

from django.shortcuts import get_object_or_404

from parking_api.config import UNIVERSITY_FEE_PERCENT
from decimal import *


# Create your views here.


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def reservationsOfUserList(request, pk):
    queryset = get_object_or_404(User, pk=pk).reservations.all()
    serializer = ReservationSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def updateBalance(request, pk, value):
    user = get_object_or_404(User, pk=pk)

    if request.user != user and not request.user.is_staff:
        return Response({'error': 'You do not have permission to perform this action'})

    user.balance.value += Decimal(value)
    user.balance.save()
    serializer = UserSerializer(user)
    return Response(serializer.data)


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsSuperUserOrReadOnly]


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsSuperUserOrReadOnly]


@api_view(['GET'])
def lotsOfEventList(request, pk):
    queryset = get_object_or_404(Event, pk=pk).lots.all()
    serializer = LotSerializer(queryset, many=True)
    return Response(serializer.data)


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


class PLotList(generics.ListCreateAPIView):
    queryset = ParentLot.objects.all()
    serializer_class = PLotSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PLotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParentLot.objects.all()
    serializer_class = PLotSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # update the count for the lot associated with the reservation
        # transfer funds from reservation owner to lot owner and university
        lot = Lot.objects.get(pk=serializer.data['lot'])
        customer = self.request.user
        lotowner = lot.owner
        admin = User.objects.get(username='admin')
        size = serializer.data['size']
        if size == 'small':
            lot.capSmallActual -= 1
            customer.balance.value -= lot.costSmall
            customer.balance.save()
            lotowner.balance.value += Decimal(1 - UNIVERSITY_FEE_PERCENT) * lot.costSmall
            lotowner.balance.save()
            admin.balance.value += Decimal(UNIVERSITY_FEE_PERCENT) * lot.costSmall
            admin.balance.save()
        elif size == 'medium':
            lot.capMediumActual -= 1
            customer.balance.value -= lot.costMedium
            customer.balance.save()
            lotowner.balance.value += Decimal(1 - UNIVERSITY_FEE_PERCENT) * lot.costMedium
            lotowner.balance.save()
            admin.balance.value += Decimal(UNIVERSITY_FEE_PERCENT) * lot.costMedium
            admin.balance.save()
        elif size == 'large':
            lot.capLargeActual -= 1
            customer.balance.value -= lot.costLarge
            customer.balance.save()
            lotowner.balance.value += Decimal(1 - UNIVERSITY_FEE_PERCENT) * lot.costLarge
            lotowner.balance.save()
            admin.balance.value += Decimal(UNIVERSITY_FEE_PERCENT) * lot.costLarge
            admin.balance.save()

        lot.save()
        customer.save()
        lotowner.save()
        admin.save()

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_destroy(self, instance):
        lot = Lot.objects.get(pk=instance.lot.id)
        customer = self.request.user
        lotowner = lot.owner
        admin = User.objects.get(username='admin')
        size = instance.size
        if size == 'small':
            lot.capSmallActual += 1
            customer.balance.value += lot.costSmall
            customer.balance.save()
            lotowner.balance.value -= Decimal(1 - UNIVERSITY_FEE_PERCENT) * lot.costSmall
            lotowner.balance.save()
            admin.balance.value -= Decimal(UNIVERSITY_FEE_PERCENT) * lot.costSmall
            admin.balance.save()
        elif size == 'medium':
            lot.capMediumActual += 1
            customer.balance.value += lot.costMedium
            customer.balance.save()
            lotowner.balance.value -= Decimal(1 - UNIVERSITY_FEE_PERCENT) * lot.costMedium
            lotowner.balance.save()
            admin.balance.value -= Decimal(UNIVERSITY_FEE_PERCENT) * lot.costMedium
        elif size == 'large':
            lot.capLargeActual += 1
            customer.balance.value += lot.costLarge
            customer.balance.save()
            lotowner.balance.value -= Decimal(1 - UNIVERSITY_FEE_PERCENT) * lot.costLarge
            lotowner.balance.save()
            admin.balance.value -= Decimal(UNIVERSITY_FEE_PERCENT) * lot.costLarge

        lot.save()

        instance.delete()
