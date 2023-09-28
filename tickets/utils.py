from rest_framework.serializers import ValidationError
from tickets.models import (
    Booking,
    Ticket
)


def validate(self, data):
    if Booking.objects.filter(
            session=data['session'],
            seat=data['seat']
    ).exists():
        raise ValidationError(
            {
                'message':
                    'This seat is already booked!'
            }
        )

    if Ticket.objects.filter(
            session=data['session'],
            seat=data['seat']
    ).exists():
        raise ValidationError(
            {
                'message':
                    'There is already a ticket for this seat!'
            }
        )

    return data
