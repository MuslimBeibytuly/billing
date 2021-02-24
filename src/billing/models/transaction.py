from decimal import Decimal

from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import Entity


class Transaction(Entity):
    amount = models.DecimalField(
        verbose_name=_('amount'),
        help_text=_('amount'), default=Decimal(0),
        max_digits=24, decimal_places=8,
    )

    class Meta:
        abstract = True
