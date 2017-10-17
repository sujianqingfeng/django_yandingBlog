#!/usr/bin/env python
# encoding: utf-8

"""
@author: su jian
@contact: 121116111@qq.com
@file: base_model.py
@time: 2017/10/17 15:58
"""

from datetime import datetime

from django.db import models


class BaseModel(models.Model):
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')
    update_time = models.DateField(default=datetime.now, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        abstract = True
