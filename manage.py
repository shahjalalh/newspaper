#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    if os.environ.get('DJANGO_ENV_FILE'):
        from newspaper.lib import utils  # noqa isort:skip

        utils.read_env_file(os.environ['DJANGO_ENV_FILE'])

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newspaper.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')

    from configurations.management import execute_from_command_line  # noqa isort:skip

    execute_from_command_line(sys.argv)
