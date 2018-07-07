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
from rest_framework.schemas import AutoSchema

from utils.permission import IsOwnerOrReadOnly
from .filters import BlogFilter
from .models import Blog
from .serializers import BlogSerializer, BlogDetailSerializer, BlogUpdateSerializer, \
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




class BlogViewSet(mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin,
                  mixins.ListModelMixin,
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
    # filter_backends = (DjangoFilterBackend,)
    # filter_class = BlogFilter

    # filter_fields = ('username',)




    def get_serializer_class(self):
        if self.action == 'list_by_id' or self.action == 'list' or self.action == 'list_by_name':
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


    @action(methods=['get'], detail=True)
    def list_by_id(self, request, pk=None):
        """
        通过id 获取blog
        """
        queryset = Blog.objects.filter(user_id=pk)
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def list_by_name(self, request, pk=None):
        """
        desc: the desc of this api.
        parameters:
        - username: mobile
          desc: the mobile number
          type: string
          required: true
          location: query
        """
        # queryset = self.filter_queryset(self.get_queryset())
        queryset = Blog.objects.filter(user__username=request.query_params.get('name'))
        # queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, serializer_class=TreeReviewSerializer, permission_classes=[])
    def reviews(self, request, pk=None):
        """
        对应blog的评论
        """

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
