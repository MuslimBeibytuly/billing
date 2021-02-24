from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from .entity import Entity


class Profile(Entity):
    user = models.OneToOneField(
        to=get_user_model(), verbose_name=_('user'), help_text=_('user'),
        on_delete=models.CASCADE, related_name='profile',
    )

    class Meta:
        db_table = 'common.profiles'
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')
