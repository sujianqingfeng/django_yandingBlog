from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from utils.permission import IsOwnerOrReadOnly
from .filters import BlogFilter
from .models import Blog
from .serializers import BlogSerializer, BlogDetailSerializer, BlogUpdateSerializer, BlogAdminSerializer, \
    BlogSimpleSerializer
from review.serializers import TreeReviewSerializer

User = get_user_model()


class BlogPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_size_query_description = '个数'
    page_query_param = 'page'
    page_query_description = '页数'
    max_page_size = 100


class BlogViewSet(mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
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
    """
    pagination_class = BlogPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    # filter_class = BlogFilter
    search_fields = ('title')
    ordering = ('add_time',)
    ordering_fields = '__all__'

    def get_serializer_class(self):
        if self.action == 'blog_list' or self.action == 'list':
            return BlogSimpleSerializer
        elif self.action == 'partial_update' or self.action == 'update':
            return BlogUpdateSerializer
        elif self.action == 'retrieve':
            return BlogDetailSerializer
        else:
            return BlogSerializer

    def get_queryset(self):
        return Blog.objects.all()

    def get_permissions(self):
        if self.action == 'blog_list' or self.action == 'retrieve':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

        return [premission() for premission in permission_classes]

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    # def perform_create(self, serializer):
    #     serializer.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status.HTTP_200_OK)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def blog_list(self, request, pk=None):
        queryset = Blog.objects.filter(user_id=pk)
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, serializer_class=TreeReviewSerializer, permission_classes=[])
    def reviews(self, request, pk=None):

        query = TreeReviewSerializer.setup_eager_loading(Blog.objects.all(),
                                                         prefetch_related=TreeReviewSerializer.PREFETCH_RELATED_FIELDS)
        blog = query.get(id=pk)
        reviews = blog.review.all()
        page = self.paginate_queryset(reviews)
        if page is not None:
            serializer = TreeReviewSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)
        serializer = TreeReviewSerializer(reviews, many=True, context={'request': request})
        return Response(serializer.data)
