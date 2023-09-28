from rest_framework.fields import SerializerMethodField
from rest_framework import serializers as szs
from movies.models import *
from datetime import date


class MovieSerializerMixin:
    status = SerializerMethodField()

    def get_status(self, obj):
        now = date.today()
        if now < obj.starting:
            obj.status = 0
            obj.save()
        elif obj.starting <= now < obj.ending:
            obj.status = 1
            obj.save()
        elif obj.ending <= now:
            obj.status = -1
            obj.save()
        return obj.status


class MovieListSerializer(szs.ModelSerializer, MovieSerializerMixin):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieCreateManageSerializer(szs.ModelSerializer, MovieSerializerMixin):
    class Meta:
        model = Movie
        fields = [
            'title',
            'poster',
            'description',
            'status'
            'age_rating',
            'year',
            'duration',
            'price',
            'starting',
            'ending'
        ]

    def validate(self, data):
        if data['starting'] >= data['ending']:
            raise szs.ValidationError(
                {
                    'error':
                        "Starting date can't be later than ending date or be equal to it."
                }
            )
        return data


class CinemaSerializer(szs.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class RoomSizeSerializer(szs.ModelSerializer):
    class Meta:
        model = RoomSize
        fields = '__all__'


class RoomSerializer(szs.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class SeatSerializer(szs.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'
