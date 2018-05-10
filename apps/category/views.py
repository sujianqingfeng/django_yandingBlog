from django.contrib.auth import get_user_model
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.category.serializers import CategoryCreateSerializer, CategoryDetailSerializer
from category.models import Category
from utils.permission import IsOwnerOrReadOnly

User = get_user_model()


class CategoryViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    '''
    category_list:
    得到所有类别

    create:
    创建类别

    detele:
    删除类别

    update:
    修改类别
    '''

    authentication_classes = (SessionAuthentication, JSONWebTokenAuthentication)

    def get_queryset(self):
        if self.action == 'category_list':
            user = User.objects.filter(id=self.kwargs['pk'])
            return Category.objects.filter(user=user)
        else:
            return Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'list':
            return CategoryCreateSerializer
        else:
            return CategoryDetailSerializer

    def get_permissions(self):
        if self.action == 'category_list':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

        return [premission() for premission in permission_classes]

    @detail_route(methods=['get'])
    def category_list(self, request, pk=None):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
