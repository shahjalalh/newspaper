import os

import pytest

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


@pytest.fixture
def data_dir():
    return DATA_DIR
