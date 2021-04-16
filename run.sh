#bin/bash

python mysite/manage.py makemigrations
python mysite/manage.py migrate
python mysite/manage.py runserver

