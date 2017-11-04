from rest_framework import mixins
from rest_framework import generics

from .models import Blog
from .serializers import BlogSerializer


class BlogListView(generics.ListAPIView):
    """
    博客列表
    """

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


