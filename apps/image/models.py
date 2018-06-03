from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

from apps.base.base_model import BaseModel

User = get_user_model()


class Image(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    url = models.ImageField(upload_to=settings.UPLOAD_DIR, null=False, blank=False, verbose_name='图片url')

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = verbose_name
