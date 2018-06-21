#!/usr/bin/env bash
cd /var/www
rm -fr django_yandingBlog
git clone https://github.com/sujianqingfeng/django_yandingBlog.git
cd django_yandingBlog
pipenv install --three
pipenv run python manage.py migrate
pipenv run python manage.py collectstatic
sudo killall -9 uwsgi
uwsgi --ini uwsgi.ini
