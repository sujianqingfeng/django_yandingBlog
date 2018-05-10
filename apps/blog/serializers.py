#!/usr/bin/env python
# encoding: utf-8

"""
@author: sujian
@contact: h121116111@gmail.com
@file: serializers.py
@time: 2017/10/27 0:39
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.models import Blog
from category.serializers import CategoryCreateSerializer
from user.serializers import UserGetSerializer
from category.models import Category



User = get_user_model()


class BlogSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    id = serializers.IntegerField(read_only=True)
    category = serializers.CharField(required=True, write_only=True)

    def create(self, validated_data):
        category = validated_data.get('category')
        content = validated_data.get('content')
        title = validated_data.get('title')

        user = self.context['request'].user
        user_id = self.context['request'].user.id
        if category.isdigit():
            if Category.objects.get(id=category) is None:
                return self.create_blog(user, category, title, content)
            else:
                return Blog.objects.create(user_id=user_id, category_id=category, title=title, content=content)
        else:
            return self.create_blog(user, category, title, content)

    def create_blog(self, user, category, title, content):
        category_instance = Category.objects.create(name=category, user=user)
        return Blog.objects.create(user=user, category=category_instance, title=title, content=content)

    class Meta:
        model = Blog
        fields = ('id', 'category', 'content', 'title', 'user')
        extra_kwargs = {
            'category': {'write_only': True},
            'content': {'write_only': True},
            'title': {'write_only': True}
        }


class BlogUpdateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    id = serializers.IntegerField(read_only=True)
    category = serializers.CharField(write_only=True)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.title = validated_data.get('title', instance.title)
        category = validated_data.get('category', instance.category)

        user = self.context['request'].user

        if category.isdigit():
            if Category.objects.get(id=category) is None:
                category_instance = Category.objects.create(name=category, user=user)
                instance.category = category_instance
                instance.save()
                return instance
            else:
                instance.category = Category.objects.get(id=category)
                instance.save()
                return instance
        else:
            try:
                category = Category.objects.get(name=category)
                instance.category = category
                instance.save()
                return instance
            except:
                category_instance = Category.objects.create(name=category, user=user)
                instance.category = category_instance
                instance.save()

                return instance

    class Meta:
        model = Blog
        fields = ('id', 'category', 'content', 'title', 'user')
        extra_kwargs = {
            'category': {'write_only': True},
            'content': {'write_only': True},
            'title': {'write_only': True}
        }


class BlogDetailSerializer(serializers.ModelSerializer):
    user = UserGetSerializer()
    category = CategoryCreateSerializer()

    class Meta:
        model = Blog
        fields = '__all__'



class BlogAdminSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category = CategoryCreateSerializer()

    class Meta:
        model = Blog
        fields = ('user','category','id','add_time','title')
