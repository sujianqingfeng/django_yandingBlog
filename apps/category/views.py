from django.contrib.auth import get_user_model
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.category.serializers import CategoryCreateSerializer, CategoryDetailSerializer
from category.models import Category
from utils.permission import IsOwnerOrReadOnly

User = get_user_model()


class CategoryViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    """
    create:
    创建类别
    detele:
    删除类别
    update:
    修改类别
    """

    def get_queryset(self):
        return Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'list':
            return CategoryCreateSerializer
        else:
            return CategoryDetailSerializer

    def get_permissions(self):
        if self.action == 'list_by_id' or self.action == 'list_by_name':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

        return [premission() for premission in permission_classes]

    @action(methods=['get'], detail=True)
    def list_by_id(self, request, pk=None):
        """
        通过id获取类别列表
        """
        queryset = Category.objects.filter(user_id=pk)
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def list_by_name(self, request, pk=None):
        """
        通过名字获取类别列表
        """
        queryset = Category.objects.filter(user__username=request.query_params.get('name'))
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
