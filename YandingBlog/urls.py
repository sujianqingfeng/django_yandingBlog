"""YandingBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
# from rest_framework.authtoken import views
# import xadmin
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from blog.views import BlogViewSet, CategoryViewSet
from user.views import UserViewset
from review.views import ReviewViewSet
from like.views import LikeViewSet

router = DefaultRouter()

router.register(r'users', UserViewset, base_name='users')
# router.register(r'categorys', CategoryViewSet, base_name='categorys')
router.register(r'blogs', BlogViewSet, base_name='bolgs')
router.register(r'reviews', ReviewViewSet, base_name='reviews')
router.register(r'like', LikeViewSet, base_name='like')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^xadmin/', xadmin.site.urls),
    url(r'doc/', include_docs_urls(title='yanding Api')),
    url(r'^login/', obtain_jwt_token),

    url(r'^', include(router.urls)),
    url(r'^ca/(?P<pk>[^/.]+)/$', CategoryViewSet.as_view(
        { 'get':'list',
          'post':'create'}
))
]
