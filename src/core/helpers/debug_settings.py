from typing import Tuple, Dict, Callable


def show_toolbar(*args, **kwargs) -> bool:
    return True


DEFAULT_DEBUG_APPS: Tuple[str, ...] = ('debug_toolbar',)
DEFAULT_DEBUG_MIDDLEWARE: Tuple[str, ...] = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
DEFAULT_DEBUG_TOOLBAR_CONFIG: Dict[str, Callable] = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}
DEFAULT_DEBUG_INTERNAL_IPS: Tuple[str, ...] = ('127.0.0.1',)
PANELS: str = 'debug_toolbar.panels.'
DEFAULT_DEBUG_TOOLBAR_PANELS: Tuple[str, ...] = (
    f'{PANELS}versions.VersionsPanel', f'{PANELS}timer.TimerPanel',
    f'{PANELS}settings.SettingsPanel', f'{PANELS}headers.HeadersPanel',
    f'{PANELS}request.RequestPanel', f'{PANELS}redirects.RedirectsPanel',
    f'{PANELS}staticfiles.StaticFilesPanel', f'{PANELS}sql.SQLPanel',
    f'{PANELS}templates.TemplatesPanel', f'{PANELS}cache.CachePanel',
    f'{PANELS}signals.SignalsPanel', f'{PANELS}logging.LoggingPanel',
)
