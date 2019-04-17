#!/usr/bin/env bash

echo "... Starting nginx"
nginx

echo "... Applying Django migrations"
python manage.py makemigrations
python manage.py migrate

echo "... Applying Django collect static"
python manage.py collectstatic --noinput

echo "... Starting Django via gunicorn"
gunicorn config.wsgi -b 0.0.0.0:8001 -w 4 --reload