#!/usr/bin/env python
# encoding: utf-8

"""
@author: su jian
@contact: 121116111@qq.com
@file: base_django.py
@time: 2017/10/17 18:58
"""

import xadmin


class GlobalSetting(object):
    site_title = '言鼎博客后台管理系统'  # 设置头标题
    site_footer = '言鼎博客'  # 设置脚标题
    menu_style = 'accordion'


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(xadmin.views.BaseAdminView, BaseSetting)

xadmin.site.register(xadmin.views.CommAdminView, GlobalSetting)
