import os

from configurations import Configuration, values


class Defaults(Configuration):
    """Base settings object, settings in this class will be shared
    over all different environments.

    """
    BASE_DIR = '/opt/newspaper/'

    DEBUG = False

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'newspaper.sqlite3',
        }
    }

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'django.contrib.sites',

        # allauth apps
        'allauth',
        'allauth.account',
        'allauth.socialaccount',

        # ... include the providers you want to enable:
        # http://django-allauth.readthedocs.io/en/latest/installation.html
        # 'allauth.socialaccount.providers.facebook',
        # 'allauth.socialaccount.providers.google',

        'newspaper',
        'newspaper.apps.users',
        'newspaper.apps.blog',
    ]

    SITE_ID = 1

    MIDDLEWARE = [
        'django.middleware.http.ConditionalGetMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.http.ConditionalGetMiddleware',
    ]

    ROOT_URLCONF = 'newspaper.urls'

    SECRET_KEY = values.SecretValue()

    @property
    def TEMPLATES(self):
        return [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [
                    os.path.join(self.BASE_DIR, 'templates'),
                ],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ]

    WSGI_APPLICATION = 'newspaper.wsgi.application'

    AUTH_USER_MODEL = 'users.User'

    AUTH_PASSWORD_VALIDATORS = [
        {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
        {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
        {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
        {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
    ]

    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'

    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    AUTHENTICATION_BACKENDS = (
        # Needed to login by username in Django admin, regardless of `allauth`
        'django.contrib.auth.backends.ModelBackend',

        # `allauth` specific authentication methods, such as login by e-mail
        'allauth.account.auth_backends.AuthenticationBackend',

    )

    REST_FRAMEWORK = {
        # Use Django's standard `django.contrib.auth` permissions,
        # or allow read-only access for unauthenticated users.
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        ],
        # 'PAGE_SIZE': 10
    }
