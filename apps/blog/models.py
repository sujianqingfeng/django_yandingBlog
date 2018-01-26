from django.db import models
from django.contrib.auth import get_user_model

from apps.base.base_model import BaseModel

User = get_user_model()



class Image(BaseModel):
    user = models.ForeignKey(User, verbose_name='用户')
    name = models.CharField(max_length=100,null=False, blank=False, verbose_name='图片名字')
    url = models.ImageField(null=False, blank=False, verbose_name='图片url')

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = verbose_name


class Category(BaseModel):
    user = models.ForeignKey(User, related_name='Category', related_query_name='Category', verbose_name='用户')
    name = models.TextField(null=False, blank=False, verbose_name='名字')

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name


class Blog(BaseModel):
    user = models.ForeignKey(User, verbose_name='用户')
    category = models.ForeignKey(Category, verbose_name='类别')
    image = models.ForeignKey(Image, verbose_name='图片')
    content = models.TextField(blank=True, verbose_name='博客正文')
    title = models.TextField(null=False, blank=False, verbose_name="标题")

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name
