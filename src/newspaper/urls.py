from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import healthcheck

urlpatterns = [
    url(r'^healthcheck/$', healthcheck, name='healthcheck'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include('newspaper.apps.blog.urls')),
]

if settings.DEBUG:
    from django.views import defaults  # noqa isort:skip
    from django.views.generic import TemplateView # noqa isort:skip

    urlpatterns.extend([
        url(r'^400$', defaults.bad_request, {'exception': ""}),
        url(r'^403$', defaults.permission_denied, {'exception': ""}),
        url(r'^404$', defaults.page_not_found, {'exception': ""}),
        url(r'^500$', defaults.server_error),
        url(r'^csrf$', TemplateView.as_view(template_name='403_csrf.html')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

    # Try to load the django-debug-toolbar if it's available.
    try:
        import debug_toolbar  # noqa isort:skip
    except ImportError:
        pass
    else:
        urlpatterns.append(
            url(r'__debug__/', include(debug_toolbar.urls)),
        )

