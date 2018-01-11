from django.db import models
from django.contrib.auth import get_user_model

from apps.base.base_model import BaseModel


User = get_user_model()

# Create your models here.

class Blog(BaseModel):
    user = models.ForeignKey(User,verbose_name='用户')
    content = models.TextField(blank=True, verbose_name='博客正文')

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客'
