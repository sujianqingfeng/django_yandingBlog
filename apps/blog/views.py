from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.contrib.auth import get_user_model
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import list_route, detail_route
from rest_framework import status
from rest_framework.settings import api_settings

from utils.permission import IsOwnerOrReadOnly
from .models import Blog, Category, Image
from .serializers import BlogSerializer, CategoryCreateSerializer, CategoryDetailSerializer, BlogDetailSerializer, \
    BlogListImgSerializer, BlogUpdateSerializer
from .filters import BlogFilter

User = get_user_model()


class BlogPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_size_query_description = '个数'
    page_query_param = 'page'
    page_query_description = '页数'
    max_page_size = 100


class BlogViewSet(mixins.DestroyModelMixin,
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
        if self.action == 'blog_list' or self.action == 'retrieve':
            return BlogDetailSerializer
        elif self.action == 'partial_update' or self.action == 'update':
            return BlogUpdateSerializer
        else:
            return BlogSerializer

    def get_queryset(self):
        if self.action == 'blog_list':
            user = User.objects.filter(id=self.kwargs['pk'])
            return Blog.objects.filter(user=user)
        else:
            return Blog.objects.get(id=self.kwargs['pk'])

    def get_permissions(self):
        if self.action == 'blog_list' or self.action=='retrieve':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

        return [premission() for premission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

    """
        Update a model instance.
        """

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data,status.HTTP_200_OK)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


    def retrieve(self, request, *args, **kwargs):
        instance = Blog.objects.get(id=self.kwargs['pk'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def blog_list(self, request, pk=None):
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


class BlogImgViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    '''
    create:
    创建图片
    '''

    authentication_classes = (SessionAuthentication, JSONWebTokenAuthentication)
    queryset = Image.objects.all()
    serializer_class = BlogListImgSerializer

    parser_classes = (MultiPartParser, FileUploadParser,)

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        return [premission() for premission in permission_classes]
