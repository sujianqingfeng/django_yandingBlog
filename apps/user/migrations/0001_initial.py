# Generated by Django 2.0.5 on 2018-06-11 15:05

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('birthday', models.DateField(blank=True, help_text='出生年月', null=True, verbose_name='出生年月')),
                ('add_time', models.DateField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间')),
                ('update_time', models.DateField(default=datetime.datetime.now, help_text='更新时间', verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, help_text='是否删除', verbose_name='是否删除')),
                ('sex', models.IntegerField(choices=[(1, '男'), (2, '女'), (3, '未知')], default=3, help_text='性别: 1(男),2(女),3(未知)', verbose_name='性别')),
                ('phone', models.CharField(blank=True, help_text='手机', max_length=11, null=True, verbose_name='手机')),
                ('icon', models.ImageField(blank=True, default='/static/images/avater.jpg', help_text='头像', null=True, upload_to='static/images/%Y/%m/%d', verbose_name='头像')),
                ('desc', models.CharField(blank=True, default='', help_text='描述', max_length=100, null=True, verbose_name='描述')),
                ('github', models.CharField(blank=True, default='', help_text='github', max_length=100, null=True, verbose_name='github')),
                ('qq', models.CharField(blank=True, default='', help_text='qq', max_length=100, null=True, verbose_name='qq')),
                ('other_link', models.CharField(blank=True, default='', help_text='其他链接', max_length=100, null=True, verbose_name='其他链接')),
                ('last_login_ip', models.GenericIPAddressField(blank=True, null=True, unpack_ipv4=True, verbose_name='最近ip')),
                ('ip_joined', models.GenericIPAddressField(blank=True, null=True, unpack_ipv4=True, verbose_name='注册')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
