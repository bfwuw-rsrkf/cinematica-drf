from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username


class DiscountCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='d_card')
    balance = models.FloatField(default=0)
    discount = models.IntegerField(default=0)

    def discount_update(self):
        total_spent = self.user.orders.tickets.filter(is_paid=True).aggregate(models.Sum('price'))['price__sum']
        if total_spent:
            if total_spent >= 10000.0:
                self.discount = 7
            elif total_spent >= 7000.0:
                self.discount = 5
            elif total_spent >= 5000.0:
                self.discount = 3
            elif total_spent >= 3000.0:
                self.discount = 1
            else:
                self.discount = 0
            self.save()

    def __str__(self):
        return f"{self.user}'s discount card"


class FeedBack(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='feedbacks')
    title = models.CharField(max_length=255)
    content = models.TextField(unique=True)
    review = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
