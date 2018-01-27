# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-27 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.IntegerField(choices=[(1, '男'), (2, '女'), (3, '未知')], default=3, help_text='性别', verbose_name='性别'),
        ),
    ]
