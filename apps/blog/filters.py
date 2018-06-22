#!/usr/bin/env python
# encoding: utf-8

from django_filters import rest_framework as filter

from blog.models import Blog, Category


class BlogFilter(filter.FilterSet):
    """
    博客过滤
    """

    title = filter.CharFilter(name='title', lookup_expr='icontains', help_text='标题')
    username = filter.CharFilter(name='username', lookup_expr='gt', help_text='名字')

    class Meta:
        model = Blog
        fields = ['title', 'username']
