from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from apps.base.base_model import BaseModel





class Image(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='用户')
    # name = models.CharField(max_length=100, null=False, blank=False, verbose_name='图片名字')
    url = models.ImageField(upload_to=settings.UPLOAD_DIR, null=False, blank=False, verbose_name='图片url')

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = verbose_name
