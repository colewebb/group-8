from rest_framework import serializers
from api.models import Event, Lot, Reservation
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    reservations = serializers.PrimaryKeyRelatedField(many=True, queryset=Reservation.objects.all())
    lots = serializers.PrimaryKeyRelatedField(many=True, queryset=Lot.objects.all())
    balance = 50

    class Meta:
        model = User
        fields = ['id', 'username', 'reservations', 'lots', 'balance']


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
