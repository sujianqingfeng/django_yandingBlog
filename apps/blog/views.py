from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.contrib.auth import get_user_model
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import list_route, detail_route

from utils.permission import IsOwnerOrReadOnly
from .models import Blog, Category
from .serializers import BlogSerializer, CategoryCreateSerializer, CategoryDetailSerializer, BlogDetailSerializer
from .filters import BlogFilter

User = get_user_model()


class BlogPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_size_query_description = '个数'
    page_query_param = 'page'
    page_query_description = '页数'
    max_page_size = 100


class BlogViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    '''
    list:
    获取博客列表

    retrieve:
    博客详情

    create:
    添加博客

    update:
    更新博客

    destroy:
    删除博客
    '''
    pagination_class = BlogPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = BlogFilter
    search_fields = ('title')
    ordering = ('add_time',)
    ordering_fields = '__all__'

    def get_serializer_class(self):
        if self.action == 'blog_list':
            return BlogDetailSerializer
        else:
            return BlogSerializer

    def get_queryset(self):
        if self.action == 'blog_list':
            user = User.objects.filter(id=self.kwargs['pk'])
            return Blog.objects.filter(user=user)
        else:
            return Blog.objects.all()

    @detail_route(methods=['get'])
    def blog_list(self,request, pk=None):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin,
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

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    authentication_classes = (SessionAuthentication, JSONWebTokenAuthentication)

    def get_queryset(self):
        if self.action == 'category_list':
            user = User.objects.filter(id=self.kwargs['pk'])
            return Category.objects.filter(user=user)
        else:
            return Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CategoryCreateSerializer
        else:
            return CategoryDetailSerializer

    @detail_route(methods=['get'])
    def category_list(self, request, pk=None):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
