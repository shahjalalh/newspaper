#!/bin/sh

#: Load required environment variables in `application.settings`
if [$DJANGO_CONFIGURATION != 'Development'];
then
    echo "TODO: Load application.settings from other source."
fi

#: Configure application
manage.py collectstatic --noinput
manage.py migrate --noinput

#: Lastly, Run uWSGI webserver
uwsgi --ini /opt/newspaper/etc/uwsgi.ini
