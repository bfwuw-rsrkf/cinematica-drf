from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from movies.models import (
    Movie,
    Cinema,
    RoomSize,
    Room,
    Seat
)
from movies.serializers import (
    MovieListSerializer,
    MovieCreateManageSerializer,
    CinemaSerializer,
    RoomSizeSerializer,
    RoomSerializer,
    SeatSerializer
)


class MovieListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer


class MovieCreateAPIView(CreateAPIView):
    serializer_class = MovieCreateManageSerializer


class MovieManageAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateManageSerializer


class CinemaListCreateAPIView(ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class CinemaManageAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class RoomSizeListCreateAPIView(ListCreateAPIView):
    queryset = RoomSize.objects.all()
    serializer_class = RoomSizeSerializer


class RoomSizeManageAPIView(RetrieveUpdateDestroyAPIView):
    queryset = RoomSize.objects.all()
    serializer_class = RoomSizeSerializer


class RoomListAPIView(ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.filter(self.kwargs.get('cinema'))


class RoomCreateAPIView(CreateAPIView):
    serializer_class = RoomSerializer


class RoomManageAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class SeatListAPIView(ListAPIView):
    serializer_class = SeatSerializer

    def get_queryset(self):
        return Seat.objects.filter(self.kwargs.get('room'))


class SeatCreateAPIView(CreateAPIView):
    serializer_class = SeatSerializer


class SeatManageAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
