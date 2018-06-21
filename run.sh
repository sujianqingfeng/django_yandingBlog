#!/usr/bin/env bash
rm -fr django_yandingBlog
git clone https://github.com/sujianqingfeng/django_yandingBlog.git
cd django_yandingBlog
pipenv install --three
pipenv run python manage.py migrate
pipenv run uwsgi --ini uwsgi.ini
