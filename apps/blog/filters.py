#!/usr/bin/env python
# encoding: utf-8

from django_filters import rest_framework as filter


from blog.models import Blog


class BlogFilter(filter.FilterSet):
    '''
    博客过滤
    '''

    title = filter.CharFilter(name='title',lookup_expr='icontains')
    class Meta:
        model = Blog
        fields = ['title']
