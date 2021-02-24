from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT

urlpatterns = i18n_patterns(
    path(route='admin/', view=admin.site.urls),
)
urlpatterns += (
    path(route='silk/', view=include(arg='silk.urls')),
    path(route='api/', view=include(arg='billing.urls')),
)

if DEBUG:
    from debug_toolbar import urls
    from django.conf.urls.static import static

    urlpatterns += (
        path(route='__debug__/', view=include(arg=urls)),
    )
    urlpatterns += tuple(
        static(prefix=MEDIA_URL, document_root=MEDIA_ROOT)
    )
