#!/usr/bin/env python
# encoding: utf-8
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_auth.registration.serializers import RegisterSerializer

from rest_framework import serializers
from django.contrib.auth import get_user_model

from utils.request import get_ip_address_from_request

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'phone', 'password')


class UserGetSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False, help_text='邮件')
    sex = serializers.ChoiceField(choices=User.SEX_TYPE)

    username = serializers.CharField(read_only=True)

    def get_sex(self, obj):
        return obj.get_sex_display()

    sex = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'phone', 'sex', 'birthday', 'email', 'desc', 'id', 'icon', 'github', 'other_link')


class UserPostSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False, help_text='邮件')
    sex = serializers.ChoiceField(choices=User.SEX_TYPE)
    username = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'phone', 'sex', 'birthday', 'email', 'desc', 'id', 'icon', 'github', 'other_link')



class UserRegistrationSerializer(RegisterSerializer):
    """
    继承至rest_auth的默认序列器，增加了昵称
    """

    def save(self, request):
        """
        改写父类的save方法，检测并存入用户的注册IP地址
        """
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        ip = get_ip_address_from_request(request)
        if ip:
            user.ip_joined = ip
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user
