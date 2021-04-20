from rest_framework import serializers
from api.models import Event, Lot, ParentLot, Reservation, Balance
from rest_framework_jwt.settings import api_settings
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
    balance = serializers.PrimaryKeyRelatedField(many=False, queryset=Balance.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'reservations', 'lots', 'balance']


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'id', 'username', 'password')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'created', 'startTime', 'endTime', 'address', 'lots',
                  'reservations']


class LotSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    name = serializers.ReadOnlyField(source='parentLot.name')
    address = serializers.ReadOnlyField(source='parentLot.address')

    class Meta:
        model = Lot
        fields = [
            'id',
            'owner',
            'name',
            'address',
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
