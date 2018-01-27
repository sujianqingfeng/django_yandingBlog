# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-27 15:35
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间')),
                ('update_time', models.DateField(default=datetime.datetime.now, help_text='更新时间', verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, help_text='是否删除', verbose_name='是否删除')),
                ('content', models.CharField(max_length=700, verbose_name='评论内容')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog', verbose_name='博客')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '评论',
            },
        ),
    ]
