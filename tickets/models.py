from django.db import models
from users.models import User
from movies.models import (
    Movie,
    Room,
    Seat
)


class SessionFormat(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Session(models.Model):
    start_time = models.DateTimeField()
    format = models.ForeignKey(SessionFormat, on_delete=models.CASCADE, related_name='sessions')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='sessions')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='sessions')

    def __str__(self):
        return f'{self.start_time} - {self.movie}'


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='bookings')
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='bookings')

    def __str__(self):
        return f'{self.user}: {self.session} - {self.seat}'


class Orders(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='orders')
    total_price = models.FloatField(default=0)

    def __str__(self):
        return self.user


class TicketType(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Ticket(models.Model):
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='tickets')
    type = models.ForeignKey(TicketType, on_delete=models.PROTECT, related_name='tickets')
    session = models.ForeignKey(Session, on_delete=models.PROTECT, related_name='tickets')
    seat = models.ForeignKey(Seat, on_delete=models.PROTECT, related_name='tickets')
    price = models.FloatField(default=0)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.orders.user}: {self.session}, {self.seat}'

    def save(self, *args, **kwargs):
        price = (
                self.type.price +
                self.session.format.price +
                self.session.movie.price +
                self.seat.room.size.price
        )
        if self.orders.user.d_card:
            discount = self.orders.user.d_card.discount
            if discount >= 1:
                price -= price // 100 * discount
        self.price = price
        super().save(*args, **kwargs)
