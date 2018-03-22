from django.db import models
from django.contrib.auth import get_user_model

from apps.base.base_model import BaseModel

User = get_user_model()



class Image(BaseModel):
    user = models.ForeignKey(User, verbose_name='用户')
    name = models.CharField(max_length=100,null=False, blank=False, verbose_name='图片名字')
    url = models.ImageField(upload_to='imgs/',null=False, blank=False, verbose_name='图片url')

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = verbose_name


class Category(BaseModel):
    user = models.ForeignKey(User,verbose_name='用户',help_text='用户')
    name = models.TextField(null=False, blank=False, verbose_name='名字',help_text='类别名字')

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name



class Blog(BaseModel):
    user = models.ForeignKey(User, verbose_name='用户',help_text='用户')
    category = models.ForeignKey(Category, verbose_name='类别',help_text='类别')
    content = models.TextField(blank=True, verbose_name='博客正文',help_text='博客正文')
    title = models.TextField(null=False, blank=False, verbose_name="标题",help_text='标题')
    num = models.IntegerField(null=True,blank=True,default=0,verbose_name='数量',help_text='数量')


    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name


class Tag(BaseModel):
    blog = models.ForeignKey(Blog, verbose_name='博客', help_text='博客')
    user = models.ForeignKey(User, verbose_name='用户', help_text='用户')
    name = models.TextField(null=False, blank=False, verbose_name='标签', help_text='标签名字')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

