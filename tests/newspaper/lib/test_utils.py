import os

from newspaper.lib import utils


def test_dist_file():
    path = utils.dist_file('path', 'to', 'example.txt')
    assert path.endswith('newspaper/path/to/example.txt')


class TestReadEnvFile(object):

    def test_read_env_file(self, data_dir):
        utils.read_env_file(os.path.join(data_dir, 'envfile.env'))

        assert os.getenv('DJANGO_TEST_VAR') == 'django-test-var'
        assert os.getenv('COMMENT') is None
        assert os.getenv('DJANGO_OTHER_VAR') == 'double-quotes'
        assert os.getenv('DJANGO_ANOTHER_VAR') == 'single-quotes'

    def test_read_env_file_notfound(self, data_dir):
        del os.environ['DJANGO_TEST_VAR']
        del os.environ['DJANGO_OTHER_VAR']
        del os.environ['DJANGO_ANOTHER_VAR']

        utils.read_env_file(os.path.join(data_dir, 'invalid.env'))
        assert os.getenv('DJANGO_TEST_VAR') is None
        assert os.getenv('DJANGO_OTHER_VAR') is None
        assert os.getenv('DJANGO_ANOTHER_VAR') is None
