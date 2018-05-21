from django.conf import settings
from django.conf.urls import include, re_path
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from about.views import AboutViewSet
from blog.views import BlogViewSet
from category.views import CategoryViewSet
from friend.views import FriendViewSet
from image.views import BlogImgViewSet
from like.views import LikeViewSet
from review.views import ReviewViewSet
from user.views import UserViewset

router = DefaultRouter()

router.register(r'users', UserViewset, base_name='users')
router.register(r'category', CategoryViewSet, base_name='categorys')
router.register(r'blogs', BlogViewSet, base_name='bolgs')
router.register(r'reviews', ReviewViewSet, base_name='reviews')
router.register(r'like', LikeViewSet, base_name='like')
router.register(r'img_upload', BlogImgViewSet, base_name='img_upload')
router.register(r'friend', FriendViewSet, base_name='friend')
router.register(r'about', AboutViewSet, base_name='about')

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'doc/', include_docs_urls(title='yanding Api')),
    re_path(r'^login/', obtain_jwt_token),
    re_path(r'^', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
