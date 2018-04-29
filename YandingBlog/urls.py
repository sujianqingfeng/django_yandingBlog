from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
# from rest_framework.authtoken import views
# import xadmin
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

from blog.views import BlogViewSet, CategoryViewSet, BlogImgViewSet
from user.views import UserViewset
from review.views import ReviewViewSet
from like.views import LikeViewSet
from friend.views import FriendViewSet

router = DefaultRouter()

router.register(r'users', UserViewset, base_name='users')
router.register(r'category', CategoryViewSet, base_name='categorys')
router.register(r'blogs', BlogViewSet, base_name='bolgs')
router.register(r'reviews', ReviewViewSet, base_name='reviews')
router.register(r'like', LikeViewSet, base_name='like')
router.register(r'img_upload', BlogImgViewSet, base_name='img_upload')
router.register(r'friend', FriendViewSet, base_name='friend')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^xadmin/', xadmin.site.urls),
    url(r'doc/', include_docs_urls(title='yanding Api')),
    url(r'^login/', obtain_jwt_token),
    url(r'^', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
