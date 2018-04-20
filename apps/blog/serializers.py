#!/usr/bin/env python
# encoding: utf-8

"""
@author: sujian
@contact: h121116111@gmail.com
@file: serializers.py
@time: 2017/10/27 0:39
"""
from rest_framework import serializers

from django.contrib.auth import get_user_model

from blog.models import Blog, Image, Category

User = get_user_model()


class CategoryCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = ('name', 'user', 'id')


class CategoryDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    update_time = serializers.DateField(read_only=True)
    add_time = serializers.DateField(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    category = serializers.CharField(required=True)



    def set_category(self, obj):
        return obj.get_sex_display()

    def get_category(self, obj):
        return obj.get_sex_display()


    def create(self, validated_data):
        category = validated_data.get('category')
        content = validated_data.get('content')
        title = validated_data.get('title')

        user = self.context['request'].user
        user_id = self.context['request'].user.id
        if category.isdigit():
            return Blog.objects.create(user_id=user_id, category_id=category, title=title, content=content)
        else:
            category_instance = Category.objects.create(name=category,user=user)
            return Blog.objects.create(user_id=user_id,category=category_instance, title=title, content=content)

    class Meta:
        model = Blog
        fields = ('category', 'content', 'title', 'user')


class BlogDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    category = CategoryCreateSerializer()

    class Meta:
        model = Blog
        fields = '__all__'


class BlogImgSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def __str__(self):
        return self.url

    class Meta:
        model = Image
        fields = ('user', 'url')


class BlogListImgSerializer(serializers.Serializer):
    imgs = serializers.ListField(
        child=serializers.FileField(max_length=100000,
                                    allow_empty_file=False,
                                    use_url=True), write_only=True
    )
    blog_imgs = serializers.ListField(
        child=serializers.CharField(max_length=100000, ), read_only=True
    )

    def create(self, validated_data):
        imgs = validated_data.get('imgs')
        images = []
        for index, url in enumerate(imgs):
            image = Image.objects.create(url=url, user=User.objects.get(id=self.context['request'].user.id))
            blog = BlogImgSerializer(image, context=self.context)
            images.append(blog.data['url'])
        return {'blog_imgs': images}
