#!/usr/bin/env python
# encoding: utf-8

from django_filters import rest_framework as filter


from blog.models import Blog,Category


class BlogFilter(filter.FilterSet):
    '''
    博客过滤
    '''

    title = filter.CharFilter(name='title',lookup_expr='icontains',help_text='标题')


    def is_valid(self):
        return self.is_bound
    class Meta:
        model = Blog
        fields = ['title']

# class CategoryListFilter(filter.FilterSet):
#     id = filter.UUIDFilter(name='id',lookup_expr='icontains',help_text = 'id')
#     class Meta:
#         model = Category
#         fields = ['id']





