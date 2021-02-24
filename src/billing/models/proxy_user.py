from django.contrib.auth.models import User, UserManager
from rest_framework.authtoken.models import Token

from .account import Account


class ProxyUserManager(UserManager):
    def _create_user(self, *args, **kwargs):
        instance = super()._create_user(*args, **kwargs)
        Account.objects.create(user=instance)
        Token.objects.create(user=instance)
        return instance


class ProxyUser(User):
    objects = ProxyUserManager()

    class Meta:
        proxy = True
