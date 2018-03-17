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
from blog.models import Category


class BlogSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


    class Meta:
        model = Blog
        fields = ('category','content','title','user')

class BlogDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Blog
        fields = '__all__'


class CategoryCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Category
        fields = ('name','user','id')


class CategoryDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    update_time = serializers.DateField(read_only=True)
    add_time = serializers.DateField(read_only=True)
    class Meta:
        model = Category
        fields = '__all__'


if __name__ == '__main__':
    pass
