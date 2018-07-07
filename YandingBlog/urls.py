from django.conf import settings
from django.conf.urls import include, re_path
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
# from rest_framework_swagger.views import get_swagger_view


from about.views import AboutViewSet
from blog.views import BlogViewSet
from category.views import CategoryViewSet
from friend.views import FriendViewSet
from image.views import BlogImgViewSet
from like.views import LikeViewSet
from oauth.views import OAuthViewSet
from review.views import ReviewViewSet
from summary_img.views import SummaryImgViewSet
from user.views import UserViewSet
from visit.views import VisitViewSet

from utils.swagger import get_swagger_view



router = DefaultRouter()

router.register(r'users', UserViewSet, base_name='users')
router.register(r'category', CategoryViewSet, base_name='categorys')
router.register(r'blogs', BlogViewSet, base_name='bolgs')
router.register(r'reviews', ReviewViewSet, base_name='reviews')
router.register(r'like', LikeViewSet, base_name='like')
router.register(r'img_upload', BlogImgViewSet, base_name='img_upload')
router.register(r'friend', FriendViewSet, base_name='friend')
router.register(r'about', AboutViewSet, base_name='about')
router.register(r'oauth', OAuthViewSet, base_name='oauth')
router.register(r'summary-img', SummaryImgViewSet, base_name='summary-img')
router.register(r'visit', VisitViewSet, base_name='visit')

schema_view = get_schema_view(title='Yanding Blog API',renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])
# schema_view = get_schema_view(title='Yanding Blog API')
# schema_view = get_swagger_view(title='Yanding Blog API')

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # re_path(r'doc/', include_docs_urls(title='yanding Api')),

    re_path(r'api/', include(router.urls)),
    re_path(r'^docs/$', schema_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
