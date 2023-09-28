from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from tickets.models import (
    SessionFormat,
    Session,
    Booking,
    Orders,
    TicketType,
    Ticket
)
from tickets.serializers import (
    SessionFormatSerializer,
    SessionSerializer,
    BookingListSerializer,
    BookingCreateSerializer,
    OrdersSerializer,
    TicketTypeSerializer,
    TicketListSerializer,
    TicketCreateSerializer
)


class SessionFormatListCreateAPIView(ListCreateAPIView):
    queryset = SessionFormat.objects.all()
    serializer_class = SessionFormatSerializer


class SessionFormatManageAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SessionFormat.objects.all()
    serializer_class = SessionFormatSerializer


class SessionListCreateAPIView(ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SessionManageAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class BookingListAPIView(ListAPIView):
    serializer_class = BookingListSerializer

    def get_queryset(self):
        return Booking.objects.filter(self.kwargs.get('session'))


class BookingCreateAPIView(CreateAPIView):
    serializer_class = BookingCreateSerializer


class OrdersListAPIView(ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class TicketTypeListCreateAPIView(ListCreateAPIView):
    queryset = TicketType.objects.all()
    serializer_class = TicketTypeSerializer


class TicketTypeManageAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TicketType.objects.all()
    serializer_class = TicketTypeSerializer


class TicketListAPIView(ListAPIView):
    serializer_class = TicketListSerializer

    def get_queryset(self):
        return Booking.objects.filter(self.kwargs.get('session'))


class TicketCreateAPIView(CreateAPIView):
    serializer_class = TicketCreateSerializer
