#!/usr/bin/env python
# encoding: utf-8


from rest_framework import serializers
from django.contrib.auth import get_user_model

from utils.request import get_ip_address_from_request

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        ip = get_ip_address_from_request(self.context['request'])

        return User.objects.create(**validated_data,ip_joined=ip)


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



