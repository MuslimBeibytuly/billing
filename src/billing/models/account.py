from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import Entity


class Account(Entity):
    user = models.OneToOneField(
        to=get_user_model(), related_name='account',
        on_delete=models.PROTECT,
        verbose_name=_('user'), help_text=_('user'),
    )
    balance = models.DecimalField(
        verbose_name=_('balance'),
        help_text=_('balance'), default=Decimal(0),
        max_digits=24, decimal_places=8,
    )

    def persist(self, value: Decimal) -> None:
        self.balance += value
        self.save(update_fields=('balance',))

    def increase(self, value: Decimal) -> None:
        self.persist(value=value)

    def decrease(self, value: Decimal) -> None:
        self.persist(value=-value)

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')
        db_table = 'billing.accounts'
