#!/usr/bin/env bash
git clone https://github.com/sujianqingfeng/django_yandingBlog.git
pipenv install --three
uwsgi --ini uwsgi.ini
