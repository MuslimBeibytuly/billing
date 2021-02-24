from django.contrib.auth import get_user_model
from django.db import models
from django.db.transaction import atomic
from django.utils.translation import gettext_lazy as _

from .transaction import Transaction


class TransferQuerySet(models.QuerySet):
    @atomic
    def create(self, to_account, user, amount, **kwargs):
        from_account = user.account
        instance = super().create(
            from_account=from_account, to_account=to_account,
            user=user, amount=amount, **kwargs,
        )
        from_account.decrease(value=amount)
        to_account.increase(value=amount)
        return instance


class Transfer(Transaction):
    user = models.ForeignKey(
        to=get_user_model(), related_name='transfers',
        on_delete=models.PROTECT,
        verbose_name=_('user'), help_text=_('user'),
    )
    from_account = models.ForeignKey(
        to='billing.Account', related_name='from_transfers',
        on_delete=models.PROTECT,
        verbose_name=_('from_account'), help_text=_('from_account'),
    )
    to_account = models.ForeignKey(
        to='billing.Account', related_name='to_transfers',
        on_delete=models.PROTECT,
        verbose_name=_('to_account'), help_text=_('to_account'),
    )
    objects = TransferQuerySet.as_manager()

    class Meta:
        verbose_name = _('transfers')
        verbose_name_plural = _('transfers')
        db_table = 'billing.transfers'
