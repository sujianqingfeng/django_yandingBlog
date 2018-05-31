#!/usr/bin/env python
# encoding: utf-8
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.db.models import Prefetch
from rest_framework import serializers

from blog.models import Blog
from review.models import Review
from utils.mixins import EagerLoaderMixin


class FlatReviewSerializer(serializers.ModelSerializer):
    review = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    parent_user = serializers.SerializerMethodField()

    def get_review(self, obj):
        review = obj.content_object
        return {
            'id': review.id,
            'title': review.title,
        }

    def get_user(self, obj):
        user = obj.user
        return {
            'id': user.id,
            'username': user.username,
        }

    def get_parent_user(self, obj):
        parent = obj.parent
        if not parent:
            return None
        user = parent.user
        return {
            'id': user.id,
            'username': user.username,
        }


    class Meta:
        model = Review
        fields = (
            'id',
            'user',
            'parent_user',
            'review',
            'submit_date',
            'comment',
        )


class TreeReviewSerializer(serializers.ModelSerializer,EagerLoaderMixin):
    descendants = FlatReviewSerializer(many=True)
    user = serializers.SerializerMethodField()

    PREFETCH_RELATED_FIELDS = [
        Prefetch('review', queryset=Review.objects.order_by('-submit_date'))
    ]

    def get_user(self, obj):
        user = obj.user
        return {
            'id': user.id,
            'username': user.username,
        }

    class Meta:
        model = Review
        fields = (
            'id',
            'content_type',
            'object_pk',
            'comment',
            'submit_date',
            'user',
            'descendants',
            'descendants_count',
        )


class ReviewCreationSerializer(serializers.ModelSerializer):
    """
    仅用于 reply 的创建
    """
    parent_user = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    def get_parent_user(self, obj):
        parent = obj.parent
        if not parent:
            return None
        user = parent.user
        return {
            'id': user.id,
            'username': user.username,
        }

    def get_user(self, obj):
        user = obj.user
        return {
            'id': user.id,
            'username': user.username
        }

    def create(self, validated_data):
        reivew_id = validated_data.get('object_pk')
        review_ctype = ContentType.objects.get_for_model(
            Blog.objects.get(id=int(reivew_id))
        )
        site = Site.objects.get_current()
        validated_data['site'] = site
        validated_data['content_type'] = review_ctype
        return super(ReviewCreationSerializer, self).create(validated_data)

    class Meta:
        model = Review
        fields = (
            'id',
            'object_pk',
            'comment',
            'parent',
            'submit_date',
            'ip_address',
            'is_public',
            'is_removed',
            'user',
            'parent_user',
        )
        read_only_fields = (
            'id',
            'submit_date',
            'ip_address',
            'is_public',
            'is_removed',
        )
