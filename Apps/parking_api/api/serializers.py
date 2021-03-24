from rest_framework import serializers
from api.models import Event, Lot, Reservation
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    reservations = serializers.PrimaryKeyRelatedField(many=True, queryset=Reservation.objects.all())
    lots = serializers.PrimaryKeyRelatedField(many=True, queryset=Lot.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'reservations', 'lots']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'created', 'startTime', 'endTime', 'address', 'lot_set',
                  'reservations']


class LotSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Lot
        fields = ['id', 'owner', 'name', 'address', 'created', 'openTime',
                  'closeTime', 'costSmall', 'capSmallActual', 'capSmallMax',
                  'costMedium', 'capMediumActual', 'capMediumMax',
                  'costLarge', 'capLargeActual', 'capLargeMax',
                  'events']


class ReservationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Reservation
        fields = ['id', 'owner', 'lot', 'size', 'date', 'event', 'created']
