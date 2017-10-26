from django.shortcuts import render

# Create your views here.


from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Blog
from .serializers import BlogSerializer


class BlogListView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = Blog.objects.all()
        serializer = BlogSerializer(snippets, many=True)
        return Response(serializer.data)
