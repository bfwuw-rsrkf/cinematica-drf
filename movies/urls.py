from django.urls import path
from movies.views import *

urlpatterns = [
    path('movie-list/', MovieListAPIView.as_view(), name='movie-list'),
    path('movie-create/', MovieCreateAPIView.as_view(), name='movie-create'),
    path('movie-manage/<int:pk>', MovieManageAPIView.as_view(), name='movie-manage'),

    path('cinema-list/', CinemaListCreateAPIView.as_view(), name='cinema-list'),
    path('cinema-manage/<int:pk>', CinemaManageAPIView.as_view(), name='cinema-manage'),

    path('r_size-list/', RoomSizeListCreateAPIView.as_view(), name='r_size-list'),
    path('r_size-manage/<int:pk>', RoomSizeManageAPIView.as_view(), name='r_size-manage'),

    path('room-list/<int:cinema>', RoomListAPIView.as_view(), name='room-list'),
    path('room-create/', RoomCreateAPIView.as_view(), name='room-create'),
    path('room-manage/<int:pk>', RoomManageAPIView.as_view(), name='room-manage'),

    path('seat-list/<int:room>', SeatListAPIView.as_view(), name='seat-list'),
    path('seat-create/', SeatCreateAPIView.as_view(), name='seat-create'),
    path('seat-manage/<int:pk>', SeatManageAPIView.as_view(), name='seat-manage'),
]
