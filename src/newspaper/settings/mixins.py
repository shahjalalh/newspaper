import os
import pkg_resources




class SentryMixin(object):
    """Sentry specific settings."""
    SENTRY_PUBLIC_KEY = None
    SENTRY_PRIVATE_KEY = None
    SENTRY_PROJECT_ID = None

    @property
    def INSTALLED_APPS(self):
        return super().INSTALLED_APPS + [
            'raven.contrib.django.raven_compat',
        ]

    @property
    def RAVEN_CONFIG(self):
        return {
            'dsn': 'threaded+https://{}:{}@sentry.shahjalal.com/{}'.format(
                self.SENTRY_PUBLIC_KEY, self.SENTRY_PRIVATE_KEY, self.SENTRY_PROJECT_ID),
            'release': pkg_resources.get_distribution('newspaper').version,
        }

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'sentry': {
                'level': 'ERROR',  # To capture more than ERROR, change to WARNING, INFO, etc.
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
                'tags': {'custom-tag': 'x'},
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'root': {
                'level': 'WARNING',
                'handlers': ['sentry'],
            },
            'newspaper': {
                'level': 'INFO',
                'handlers': ['sentry', 'console'],
                'propagate': True
            },
            'django.request': {
                'handlers': ['console'],
                'level': 'ERROR',
                'propagate': True,
            },
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': True,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
        },
    }
