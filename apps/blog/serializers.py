#!/usr/bin/env python
# encoding: utf-8

"""
@author: sujian
@contact: h121116111@gmail.com
@file: serializers.py
@time: 2017/10/27 0:39
"""
from rest_framework import serializers
from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    update_time = serializers.DateField(read_only=True)
    class Meta:
        model = Blog
        fields = ('content', 'add_time', 'update_time','user')


if __name__ == '__main__':
    pass
