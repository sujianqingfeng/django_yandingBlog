#!/usr/bin/env python
# encoding: utf-8

"""
@author: sujian
@contact: h121116111@gmail.com
@file: views_base.py
@time: 2017/10/26 23:36
"""

from django.views.generic.base import View
from blog.models import Blog


class BolgListView(View):
    def get(self, request):
        blogs = Blog.objects.all()[:5]

        # from django.core.serializers import serialize
        # json_data = serialize('json', blogs)
        json_data = {'sujian': 'hello'}

        from django.http import JsonResponse
        import json
        return JsonResponse(json_data, safe=False)


if __name__ == '__main__':
    pass
