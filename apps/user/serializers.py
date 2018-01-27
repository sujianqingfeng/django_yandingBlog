#!/usr/bin/env python
# encoding: utf-8

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username','phone','password')


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=False,help_text='邮件')

    class Meta:
        model = User
        fields = ('username','phone','sex','birthday','email')