#!/usr/bin/env python
# encoding: utf-8

from rest_framework import serializers

from review.models import Review

class ReviewSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = ('user','blog', 'content')



