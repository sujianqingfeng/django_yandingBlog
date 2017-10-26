#!/usr/bin/env python
# encoding: utf-8

"""
@author: sujian
@contact: h121116111@gmail.com
@file: serializers.py
@time: 2017/10/27 0:39
"""
from rest_framework import serializers


class BlogSerializer(serializers.Serializer):
    content = serializers.models.TextField()


if __name__ == '__main__':
    pass
