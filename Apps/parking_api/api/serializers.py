from rest_framework import serializers
from api.models import Event, Lot, Spot, Reservation
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
        fields = ['name', 'created', 'startTime', 'endTime', 'address']


class LotSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Lot
        fields = ['owner', 'name', 'address', 'created', 'openTime',
                  'closeTime', 'capacityActual', 'capacityMax',
                  'events']


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = ['lot', 'size', 'cost', 'reserved']


class ReservationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Reservation
        fields = ['owner', 'spot', 'date', 'event', 'created']
