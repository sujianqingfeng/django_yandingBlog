#!/usr/bin/env python
# encoding: utf-8

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('username','phone','password')