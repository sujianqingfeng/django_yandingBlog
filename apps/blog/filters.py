#!/usr/bin/env python
# encoding: utf-8
import coreapi
from django_filters import rest_framework as filter
from rest_framework.filters import BaseFilterBackend

from blog.models import Blog, Category


class BlogFilter(filter.FilterSet):
    """
    博客过滤
    """

    title = filter.CharFilter(lookup_expr='icontains', help_text='标题')
    username = filter.CharFilter(lookup_expr='gt', help_text='名字')

    class Meta:
        model = Blog
        fields = ['title', 'username']


