#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata rates/fixtures/initial_data.json

python manage.py runserver
