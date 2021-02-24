from django.utils.translation import gettext_lazy as _

from common.apps import CommonConfig


def test_apps() -> None:
    assert 'common' == CommonConfig.name
    assert _('common') == CommonConfig.verbose_name
