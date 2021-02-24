from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommonConfig(AppConfig):
    name: str = 'common'
    verbose_name: str = _('common')
