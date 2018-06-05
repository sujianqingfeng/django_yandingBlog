#!/usr/bin/env python
# encoding: utf-8


from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.user.serializers import UserGetSerializer, UserPostSerializer
from review.serializers import FlatReviewSerializer

User = get_user_model()


class UserViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """

    read:
    得到用户信息

    """

    def get_object(self):
        return self.request.user

    def get_permissions(self):
        if self.action == 'create' or self.action == 'retrieve':
            permission_classes = []
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [premission() for premission in permission_classes]

    def get_serializer_class(self):

        if self.action == 'retrieve':
            return UserGetSerializer
        else:
            return UserPostSerializer

    def get_queryset(self):
        return User.objects.all()

    @action(methods=['get'], detail=True, serializer_class=FlatReviewSerializer)
    def reviews(self, request, pk=None):
        """
        用户的评论信息
        """
        user = self.get_object()

        reivews = user.review_comments.all()
        page = self.paginate_queryset(reivews)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = FlatReviewSerializer(reivews, many=True, context={'request': request})
        return Response(serializer.data)
