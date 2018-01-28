from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.contrib.auth import get_user_model

from .models import Blog,Category
from .serializers import BlogSerializer,CategoryCreateSerializer,CategoryDetailSerializer
from .filters import BlogFilter


User = get_user_model()

class BlogPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_size_query_description = '个数'
    page_query_param = 'page'
    page_query_description = '页数'
    max_page_size = 100


class BlogViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
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
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    pagination_class = BlogPagination
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter,)
    filter_class = BlogFilter
    search_fields = ('title')
    ordering = ('add_time',)
    ordering_fields = '__all__'




class CategoryViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    '''
    list:
    得到所有类别

    create:
    创建类别

    detele:
    删除类别

    update:
    修改类别
    '''



    def get_serializer_class(self):

        if self.action == 'create':
            return CategoryCreateSerializer
        else:
            return CategoryDetailSerializer

    def get_queryset(self):
        if self.action == 'list':
            user = User.objects.filter(id=self.kwargs['pk'])
            return Category.objects.filter(user=user)



    def cat(self, request, *args, **kwargs):

        return Response({'111':''})








