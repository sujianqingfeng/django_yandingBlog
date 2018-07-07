#!/usr/bin/env python
# encoding: utf-8


from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.user.serializers import UserDetaiilSerializer, UserPostSerializer,UserSimpleSerializer
from review.serializers import FlatReviewSerializer

User = get_user_model()


class UserViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """

    read:
    得到用户信息

    """

    def get_permissions(self):
        if self.action == 'create' or self.action == 'retrieve' or self.action=='infos_by_name':
            permission_classes = []
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [premission() for premission in permission_classes]

    def get_serializer_class(self):

        if self.action == 'retrieve' or self.action == 'infos':
            return UserDetaiilSerializer
        elif self.action == 'infos_by_name':
            return UserSimpleSerializer
        else:
            return UserPostSerializer

    def get_queryset(self):
        return User.objects.all()

    @action(methods=['get'], detail=False)
    def infos(self, request, pk=None):
        """
        用户信息
        """
        user = request.user
        serializer = self.get_serializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'],detail=False)
    def infos_by_name(self,request,pk=None):
        """
        通过名字获取用户信息
        """
        username =request.query_params.get('name')
        user = User.objects.get(username=username)
        serializer = self.get_serializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    @action(methods=['get'], detail=True, serializer_class=FlatReviewSerializer)
    def reviews(self, request, pk=None):
        """
        用户的评论信息
        """
        user = self.get_object()

        reivews = user.review_comments.all()
        page = self.paginate_queryset(reivews)
        if page is not None:
            serializer = FlatReviewSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = FlatReviewSerializer(reivews, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
