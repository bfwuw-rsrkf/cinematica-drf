from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, password, **kwargs):
        from tickets.models import Orders
        user = self.model(**kwargs)
        user.set_password(password)
        user.save()
        Orders.objects.create(user=user)
        return user

    def create_superuser(self, password, **kwargs):
        user = self.create_user(password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
