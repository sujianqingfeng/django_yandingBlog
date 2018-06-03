from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

from base.base_model import BaseModel

User = get_user_model()


class SummaryImg(BaseModel):
    """
    摘要图片 如果blog没有摘要图片 就从当中随机选取一张
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    sumary_url = models.ImageField(null=False, blank=False, upload_to=settings.UPLOAD_DIR, verbose_name='图片url',
                                   help_text='图片url')

    class Meta:
        verbose_name = '摘要图片'
        verbose_name_plural = verbose_name
