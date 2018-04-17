#!/usr/bin/env python
# encoding: utf-8

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'phone', 'password')


class UserIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('icon',)


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False, help_text='邮件')
    sex = serializers.ChoiceField(choices=User.SEX_TYPE)

    username = serializers.CharField(read_only=True)


    def get_sex(self, obj):
        return obj.get_sex_display()

    sex = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'phone', 'sex', 'birthday', 'email', 'desc', 'id', 'icon','github','other_link')
