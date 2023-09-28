from rest_framework.fields import SerializerMethodField
from rest_framework import serializers as szs
from tickets.models import *
from tickets.utils import validate


class SessionFormatSerializer(szs.ModelSerializer):
    class Meta:
        model = SessionFormat
        fields = '__all__'


class SessionSerializer(szs.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'


class BookingListSerializer(szs.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class BookingCreateSerializer(szs.ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Booking
        fields = [
            'user'
            'session',
            'seat'
        ]

    def get_user(self, obj):
        return self.context['request'].user.id

    def validate(self, data):
        return validate(self, data)


class OrdersSerializer(szs.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class TicketTypeSerializer(szs.ModelSerializer):
    class Meta:
        model = TicketType
        fields = '__all__'


class TicketListSerializer(szs.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class TicketCreateSerializer(szs.ModelSerializer):
    orders = SerializerMethodField()
    price = szs.FloatField(read_only=True)
    is_paid = szs.BooleanField(read_only=True)

    class Meta:
        model = Ticket
        fields = [
            'orders',
            'type',
            'session',
            'seat',
            'price',
            'is_paid'
        ]

    def get_orders(self, obj):
        return self.context['request'].user.orders.id

    def validate(self, data):
        return validate(self, data)
