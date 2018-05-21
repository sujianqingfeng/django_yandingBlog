from django.db import models
from django.contrib.auth import get_user_model

from apps.base.base_model import BaseModel

User = get_user_model()





class Category(BaseModel):
    user = models.ForeignKey(User, verbose_name='用户', help_text='用户',on_delete=models.CASCADE)
    name = models.TextField(null=False, blank=False, verbose_name='名字', help_text='类别名字')

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name