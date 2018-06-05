#!/usr/bin/env python
# encoding: utf-8


from rest_framework import serializers
from django.contrib.auth import get_user_model

from utils.request import get_ip_address_from_request

User = get_user_model()


class UserLoginOrRegisterSerializer(serializers.ModelSerializer):
    """
    登陆 注册 序列化
    """

    def create(self, validated_data):
        ip = get_ip_address_from_request(self.context['request'])

        return User.objects.create(**validated_data, ip_joined=ip)

    username = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')


class UserGetSerializer(serializers.ModelSerializer):
    sex = serializers.SerializerMethodField()
    today = serializers.SerializerMethodField()
    yesterday = serializers.SerializerMethodField()
    blog_num = serializers.SerializerMethodField()

    def get_blog_num(self, obj):
        return obj.blog_set.all().count()

    def get_today(self, obj):
        return obj.visit_set.get_this_day().count()

    def get_yesterday(self, obj):
        return obj.visit_set.get_yesterday().count()

    def get_sex(self, obj):
        return obj.get_sex_display()

    class Meta:
        model = User
        fields = (
            'username', 'phone', 'sex', 'birthday', 'email', 'desc', 'id', 'icon', 'github', 'other_link', 'today',
            'yesterday','blog_num')


class UserPostSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False, help_text='邮件')
    sex = serializers.ChoiceField(choices=User.SEX_TYPE)
    username = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'phone', 'sex', 'birthday', 'email', 'desc', 'id', 'icon', 'github', 'other_link')
