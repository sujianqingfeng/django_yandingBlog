#!/usr/bin/env python
# encoding: utf-8


from rest_framework import serializers
from django.contrib.auth import get_user_model

from utils.request import get_ip_address_from_request
from category.serializers import CategoryDetailSerializer

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


class UserDetaiilSerializer(serializers.ModelSerializer):
    """
    详细信息 适用于管理界面获取用户
    """
    sex = serializers.SerializerMethodField()
    today = serializers.SerializerMethodField()
    yesterday = serializers.SerializerMethodField()
    blog_num = serializers.SerializerMethodField()
    categorys = serializers.SerializerMethodField()

    def get_categorys(self, obj):
        datas = obj.category_set.all()
        serializer = CategoryDetailSerializer(datas, many=True)
        return serializer.data

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
            'yesterday', 'blog_num', 'categorys')


class UserSimpleSerializer(serializers.ModelSerializer):
    """
    用户的简单信息 适用于附带于blog列表上
    """
    class Meta:
        model = User
        fields = ('username','id', 'icon','github', 'other_link')


class UserPostSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False, help_text='邮件')
    sex = serializers.ChoiceField(choices=User.SEX_TYPE)
    username = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'phone', 'sex', 'birthday', 'email', 'desc', 'id', 'icon', 'github', 'other_link')
