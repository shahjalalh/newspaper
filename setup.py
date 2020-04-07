import json

from setuptools import Command
from setuptools import find_packages, setup
from setuptools.command.sdist import sdist as _sdist


class sdist(_sdist):
    def run(self):
        self.run_command('yarn')
        _sdist.run(self)


class yarn(Command):
    user_options = []

    def run(self):
        self.spawn('yarn install --ignore-engines --production'.split())

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


with open('package.json', 'r') as fh:
    package_json = json.load(fh)

docs_require = [
    'sphinx',
    'sphinx_rtd_theme',
]

debug_require = [
    'django-debug-toolbar',
    'flake8',
    'ipdb',
    'isort',
]

tests_require = [
    'factory-boy',
    'mock',
    'pytest',
    'pytest-cov',
    'pytest-django',
]

setup(
    author=package_json['author'],
    author_email='shahjalal.tipu@gmail.com',
    name=package_json['name'],
    description=package_json['description'],
    version=package_json['version'],
    url='https://github.com/',
    install_requires=[
        'dj-database-url==0.4.2',
        'django>=1.11.28',
        'django-configurations==2.0',
        'django-allauth==0.32.0',
        'django-filter==1.0.2',
        'django-guardian==1.4.8',
        # 'django-axes==2.3.2',
        'markdown==2.6.8',
        'whitenoise==3.3.0',
    ],
    extras_require={
        'test': tests_require,
        'docs': docs_require,
        'dev': debug_require + tests_require + docs_require,
    },
    tests_require=tests_require,
    scripts=['manage.py'],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    license='',
    classifiers=[
        'Private :: Do Not Upload',
        'License :: Other/proprietary License',
    ],
    zip_safe=False,
    cmdclass={
        'sdist': sdist,
        'yarn': yarn,
    }
)
