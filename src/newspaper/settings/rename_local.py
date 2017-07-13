from configurations import Configuration, values


class LocalSettings(object):
    DEBUG = True

    # DEBUG_TOOLBAR_ENABLED = True

    LANGUAGE_CODE = 'en-EN'

    DATABASES = values.DatabaseURLValue('pgsql://postgres:postgres@127.0.0.1/databasename')

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'shahjalal@gmail.com'
    EMAIL_HOST_PASSWORD = '********'
    DEFAULT_FROM_EMAIL = 'shahjalal@gmail.com'
