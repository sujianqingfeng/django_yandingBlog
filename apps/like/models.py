from django.db import models
from django.contrib.auth import get_user_model

from base.base_model import BaseModel
from blog.models import Blog

User = get_user_model()

class Like(BaseModel):

    user = models.ForeignKey(User,verbose_name='用户')
    blog = models.ForeignKey(Blog,verbose_name='博客')


    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name