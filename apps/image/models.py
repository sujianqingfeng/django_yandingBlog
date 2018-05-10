from django.db import models
from django.contrib.auth import get_user_model

from apps.base.base_model import BaseModel

User = get_user_model()




class Image(BaseModel):
    user = models.ForeignKey(User, verbose_name='用户')
    # name = models.CharField(max_length=100, null=False, blank=False, verbose_name='图片名字')
    url = models.ImageField(upload_to='static/images/%Y/%m/%d', null=False, blank=False, verbose_name='图片url')

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = verbose_name
