from rest_framework import generics, permissions, status
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Event, Lot, ParentLot, Reservation
from .serializers import EventSerializer, LotSerializer, PLotSerializer, ReservationSerializer
from .serializers import UserSerializer, UserSerializerWithToken, RegisterSerializer
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly, IsSuperUserOrReadOnly, IsOwner, IsSuperUser, IsSuperUserOrCreateOnly

from django.shortcuts import get_object_or_404


# Create your views here.


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    permission_classes = (permissions.AllowAny,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def reservationsOfUserList(request, pk):
    queryset = get_object_or_404(User, pk=pk).reservations.all()
    serializer = ReservationSerializer(queryset, many=True)
    return Response(serializer.data)


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsSuperUserOrReadOnly]


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsSuperUserOrReadOnly]


@api_view(['GET'])
def lotsOfEventList(request, pk):
    queryset = get_object_or_404(Event, pk=pk).lots.all()
    serializer = LotSerializer(queryset, many=True)
    return Response(serializer.data)


class LotList(generics.ListCreateAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly]


class PLotList(generics.ListCreateAPIView):
    queryset = ParentLot.objects.all()
    serializer_class = PLotSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PLotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParentLot.objects.all()
    serializer_class = PLotSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsOwner]

#
# class ReservationList(generics.ListAPIView):
#     queryset = Reservation.objects.all()
#     serializer_class = ReservationSerializer
#     permission_classes = [permissions.IsAuthenticated,
#                           IsSuperUser]


class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # update the count for the lot associated with the reservation
        lot = Lot.objects.get(pk=serializer.data['lot'])
        size = serializer.data['size']
        if size == 'small':
            lot.capSmallActual -= 1
        elif size == 'medium':
            lot.capMediumActual -= 1
        elif size == 'large':
            lot.capLargeActual -= 1

        lot.save()


class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_destroy(self, instance):
        lot = Lot.objects.get(pk=instance.lot.id)
        size = instance.size
        if size == 'small':
            lot.capSmallActual += 1
        elif size == 'medium':
            lot.capMediumActual += 1
        elif size == 'large':
            lot.capLargeActual += 1

        lot.save()

        instance.delete()
