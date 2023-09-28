from django.db import models
from django.core.validators import MinValueValidator


class Movie(models.Model):
    STATUS_CHOICES = [
        (0, 'Will be film!'),
        (1, 'Is now film)'),
        (-1, 'No more film(')
    ]

    AGE_RATING_CHOICES = [
        (1, 'G'),
        (2, 'PG'),
        (3, 'PG-13'),
        (4, 'R'),
        (5, 'NC-17')
    ]

    title = models.CharField(max_length=200, unique=True)
    poster = models.ImageField(upload_to='cinematica/movies/movie/posters', blank=True, null=True)
    description = models.TextField(unique=True)
    status = models.IntegerField(choices=STATUS_CHOICES)
    age_rating = models.IntegerField(choices=AGE_RATING_CHOICES)
    year = models.IntegerField(validators=[MinValueValidator(1875)])
    duration = models.CharField(max_length=80)
    price = models.FloatField()
    starting = models.DateField()
    ending = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Cinema(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=128, unique=True)
    schedule = models.CharField(max_length=80)
    contact = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class RoomSize(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Room(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=255)
    size = models.ForeignKey(RoomSize, on_delete=models.CASCADE, related_name='rooms')

    def __str__(self):
        return f'{self.cinema} - {self.name}'


class Seat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='seats')
    row = models.IntegerField()
    num = models.IntegerField()

    def __str__(self):
        return f'{self.room} - {self.row}/{self.num}'
