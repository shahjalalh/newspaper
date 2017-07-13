import os
import uuid

from pkg_resources import get_distribution

from . import mixins
from .defaults import Defaults


class Base(Defaults):
    WITH_DEBUG_URLS = False

    @property
    def STATIC_ROOT(self):
        return os.path.join(self.BASE_DIR, 'public', 'static')

    @property
    def MEDIA_ROOT(self):
        return os.path.join(self.BASE_DIR, 'public', 'media')

    @property
    def STATIC_URL(self):
        static_url = '/static/{}/'
        if self.WITH_DEBUG_URLS:
            return static_url.format(uuid.uuid4())
        return static_url.format(get_distribution('newspaper').version)

    MEDIA_URL = '/media/'


class BaseDevelopment(Base):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    DEBUG = True
    WITH_DEBUG_URLS = True

    SECRET_KEY = 'CHANGEME!!'

    INTERNAL_IPS = ['127.0.0.1']
    DEBUG_TOOLBAR_ENABLED = False
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        # 'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        # 'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        # 'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        # 'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
        # 'debug_toolbar.panels.profiling.ProfilingPanel',
    ]

    @property
    def TEMPLATES(self):
        templates = super().TEMPLATES
        templates[0]['OPTIONS']['debug'] = True
        return templates

    @property
    def INSTALLED_APPS(self):
        apps = ['whitenoise.runserver_nostatic']
        if self.DEBUG_TOOLBAR_ENABLED:
            apps.insert(0, 'debug_toolbar')
        return apps + super().INSTALLED_APPS

    @property
    def MIDDLEWARE(self):
        middleware = super().MIDDLEWARE
        if self.DEBUG_TOOLBAR_ENABLED:
            middleware.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
        return middleware


class Testing(mixins.SentryMixin, Base):
    ALLOWED_HOSTS = []

    WITH_DEBUG_URLS = True

    SENTRY_PUBLIC_KEY = 'CHANGEME!!'
    SENTRY_PRIVATE_KEY = 'CHANGEME!!'
    SENTRY_PROJECT_ID = 'CHANGEME!!'


class Staging(mixins.SentryMixin, Base):
    ALLOWED_HOSTS = []

    SENTRY_PUBLIC_KEY = 'CHANGEME!!'
    SENTRY_PRIVATE_KEY = 'CHANGEME!!'
    SENTRY_PROJECT_ID = 'CHANGEME!!'


class Acceptance(mixins.SentryMixin, Base):
    ALLOWED_HOSTS = []

    SENTRY_PUBLIC_KEY = 'CHANGEME!!'
    SENTRY_PRIVATE_KEY = 'CHANGEME!!'
    SENTRY_PROJECT_ID = 'CHANGEME!!'


class Production(mixins.SentryMixin, Base):
    ALLOWED_HOSTS = []

    SENTRY_PUBLIC_KEY = 'CHANGEME!!'
    SENTRY_PRIVATE_KEY = 'CHANGEME!!'
    SENTRY_PROJECT_ID = 'CHANGEME!!'
