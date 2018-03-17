#!/usr/bin/env python
# encoding: utf-8
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from like.models import Like
from blog.serializers import BlogSerializer

class LikeCreateSerializer(serializers.ModelSerializer):

    user  = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        validators = UniqueTogetherValidator(
            queryset=Like.objects.all(),
            fields=['user', 'blog'],
            message='收藏了'
        )
        fields = ('user','blog','id')


class LikeDetailSerializer(serializers.ModelSerializer):
    blog = BlogSerializer()
    class Meta:
        model = Like
        fields = ('blog', 'id')