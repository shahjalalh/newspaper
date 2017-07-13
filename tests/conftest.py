from __future__ import absolute_import

import os
import random
import shutil
import tempfile

from django.conf import settings
from django.test.utils import override_settings

pytest_plugins = 'tests.fixtures'


def pytest_configure(config):
    media_root = os.path.join(tempfile.gettempdir(), 'newspaper-media-%d' % random.getrandbits(8))

    if os.path.exists(media_root):
        shutil.rmtree(media_root)

    override = override_settings(
        MEDIA_ROOT=media_root,
    )
    override.enable()


def pytest_unconfigure(config):
    if os.path.exists(settings.MEDIA_ROOT):
        shutil.rmtree(settings.MEDIA_ROOT)
