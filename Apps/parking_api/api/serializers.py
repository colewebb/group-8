from rest_framework import serializers
from api.models import Event, Lot, ParentLot, Reservation
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

    class Meta:
        model = User
        fields = ['id', 'username', 'reservations', 'lots']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'created', 'startTime', 'endTime', 'address', 'lots',
                  'reservations']


class LotSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    name = serializers.ReadOnlyField(source='parentLot.name')

    class Meta:
        model = Lot
        fields = [
            'id',
            'owner',
            'name',
            'created',
            'openTime', 'closeTime',
            'costSmall', 'capSmallActual', 'capSmallMax',
            'costMedium', 'capMediumActual', 'capMediumMax',
            'costLarge', 'capLargeActual', 'capLargeMax',
            'event',
            'parentLot'
        ]


class PLotSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ParentLot
        fields = ['id', 'owner', 'name', 'address', 'created',
                  'capSmallMax',
                  'capMediumMax',
                  'capLargeMax',
                  ]


class ReservationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Reservation
        fields = ['id', 'owner', 'lot', 'size', 'date', 'event', 'created']
