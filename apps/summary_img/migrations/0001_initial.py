# Generated by Django 2.0.5 on 2018-06-11 15:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SummaryImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, help_text='更新时间', verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, help_text='是否删除', verbose_name='是否删除')),
                ('sumary_url', models.ImageField(help_text='图片url', upload_to='static/images/%Y/%m/%d', verbose_name='图片url')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '摘要图片',
                'verbose_name_plural': '摘要图片',
            },
        ),
    ]
