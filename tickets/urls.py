from django.urls import path
from tickets.views import *

urlpatterns = [
    path('s_format-list/', SessionFormatListCreateAPIView.as_view(), name='s_format-list'),
    path('s_format-manage/<int:pk>', SessionFormatManageAPIView.as_view(), name='s_format-manage'),

    path('session-list/', SessionListCreateAPIView.as_view(), name='session-list'),
    path('session-manage/<int:pk>', SessionManageAPIView.as_view(), name='session-manage'),

    path('book-list/<int:session>', BookingListAPIView.as_view(), name='book-list'),
    path('book-create/', BookingListAPIView.as_view(), name='book-create'),

    path('orders-list/', OrdersListAPIView.as_view(), name='orders-list'),

    path('t_type-list/', TicketTypeListCreateAPIView.as_view(), name='t_type-list'),
    path('t_type-manage/', TicketTypeManageAPIView.as_view(), name='t_type-manage'),

    path('ticket-list/<int:session>', TicketListAPIView.as_view(), name='ticket-list'),
    path('ticket-create/', TicketCreateAPIView.as_view(), name='ticket-create'),
]
