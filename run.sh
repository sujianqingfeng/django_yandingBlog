#!/usr/bin/env bash
cd /var/www

if [ -d "/var/www/django_yandingBlog/" ];then
cd django_yandingBlog
git pull
else
git clone https://github.com/sujianqingfeng/django_yandingBlog.git
cd django_yandingBlog
fi

pipenv install --three
pipenv run python manage.py migrate
pipenv run python manage.py collectstatic
sudo killall -9 uwsgi
uwsgi --ini uwsgi.ini
