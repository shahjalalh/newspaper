FROM python:3.5-alpine
MAINTAINER Shahjalal <shahjalal.tipu@gmail.com>

WORKDIR /opt/newspaper/
ENV DJANGO_ENV_FILE /opt/newspaper/etc/application.settings

RUN apk update && \
    apk add curl mailcap gettext make postgresql-dev musl-dev gcc linux-headers libjpeg-turbo-dev zlib-dev libffi-dev

ADD ./dist /tmp
ADD ./docker /opt/newspaper/etc

RUN chmod +x /opt/newspaper/etc/entrypoint.sh && \
    pip install --upgrade uwsgi `find /tmp/ -name '*.tar.gz' | tail -1` --use-wheel

EXPOSE 80
HEALTHCHECK --interval=30s --timeout=1s --retries=3 CMD curl --fail http://localhost/healthcheck || exit 1

ENTRYPOINT /opt/newspaper/etc/entrypoint.sh
