import os

if os.environ.get('DJANGO_ENV_FILE'):
    from .lib import utils  # noqa isort:skip

    utils.read_env_file(os.environ['DJANGO_ENV_FILE'])

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newspaper.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')

from configurations.wsgi import get_wsgi_application  # noqa isort:skip

application = get_wsgi_application()
