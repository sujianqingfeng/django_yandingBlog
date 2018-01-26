from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


from .models import Blog,Category
from .serializers import BlogSerializer,CategorySerializer
from .filters import BlogFilter


class BlogPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_size_query_description = '一页多少个'
    page_query_param = 'page'
    page_query_description = '页数'
    max_page_size = 100


class BlogViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    '''
    list:
        获取博客列表
    '''
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    pagination_class = BlogPagination
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter,)
    filter_class = BlogFilter
    search_fields = ('title')
    ordering = ('add_time',)
    ordering_fields = '__all__'




class CategoryViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()










