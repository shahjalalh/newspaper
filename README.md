# newspaper

A newspaper app

## Requirements

 * Python 3.5
 * PostgreSQL > 9.3
 * Node.JS 6.9.3
 * Yarn > 0.19

## Features
- django-allauth
- djangorestframework

## Installation

Create a virtualenv (assuming you have virtualenvwrapper installed)

    mkvirtualenv newspaper

To install the required python and node dependencies run:

    make develop

A superuser can be created via

    ./manage.py createsuperuser

## Development

After creating a feature make sure the `CHANGELOG.md` gets updated with the new feature.
When issuing a release make sure the version number in `package.json` gets bumped.

### Running tests

To run the complete test suite, use

	make test


For quickly running the tests, with keeping the database intact use

	make qt

To determine the actual test coverage use

	make coverage


### Linting

Make sure your project is linted using `flake8` this can be checked via

	make lint

### Import Sorting

Make sure your imports are sorted via `isort` to do this use

	make isort

### Documentation

This project should be documented using `Sphinx` source files are located in the /docs/ folder.
To generate a build of the documentation use

	make docs

### Translations

*Note: gettext should be installed before using this `brew install gettext && brew link --force gettext`*

Translations are included via .po and .mo files, translated via `gettext`.
Make sure all text within this project is in `English` and translated via `gettext`.

To collect all `translatable` strings in the project use

	make makemessages

The .po files will be created `src/newspaper/locale/**/django.po` by this and can be edited with a text editor or [PoEdit](https://poedit.net/).
After translating these files you can generate the compiled .mo files using

	make compilemessages
