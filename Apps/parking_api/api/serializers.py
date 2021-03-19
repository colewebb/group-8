from rest_framework import serializers
from api.models import Event, Lot, Spot, Reservation

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'created', 'startTime', 'endTime', 'address']


class LotSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = Reservation
        fields = ['user', 'spot', 'date', 'event', 'created']
