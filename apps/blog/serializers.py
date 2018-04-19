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


from blog.models import Blog,Image,Category
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


    class Meta:
        model = Image
        fields = ('user', 'url')


class BlogListImgSerializer(serializers.Serializer):
    imgs = serializers.ListField(
        child=serializers.FileField(max_length=100000,
                                    allow_empty_file=False,
                                    use_url=False)
    )

    def create(self, validated_data):
        imgs = validated_data.get('imgs')
        for url in imgs:

            image = Image.objects.create(url=url,user=User.objects.get(id=self.context['request'].user.id))
            image.save()

        return validated_data




if __name__ == '__main__':
    pass
