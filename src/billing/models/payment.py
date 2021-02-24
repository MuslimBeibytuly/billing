from django.contrib.auth import get_user_model
from django.db import models
from django.db.transaction import atomic
from django.utils.translation import gettext_lazy as _

from .transaction import Transaction


class PaymentQuerySet(models.QuerySet):
    @atomic
    def create(self, user, **kwargs):
        account = user.account
        instance = super().create(
            user=user, account=account, **kwargs,
        )
        account.increase(value=instance.amount)
        return instance


class Payment(Transaction):
    user = models.ForeignKey(
        to=get_user_model(), related_name='payments',
        on_delete=models.PROTECT,
        verbose_name=_('user'), help_text=_('user'),
    )
    account = models.ForeignKey(
        to='billing.Account', related_name='payments',
        on_delete=models.PROTECT,
        verbose_name=_('account'), help_text=_('account'),
    )
    objects = PaymentQuerySet.as_manager()

    class Meta:
        verbose_name = _('payment')
        verbose_name_plural = _('payments')
        db_table = 'billing.payments'
