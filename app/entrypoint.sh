#!/bin/sh

python3 manage.py makemigrations && python3 manage.py migrate 


python manage.py collectstatic --no-input
gunicorn sba.wsgi:application --workers=4 --timeout 120 --bind=0.0.0.0:8000