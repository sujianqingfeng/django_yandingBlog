from django.db import models
from django.contrib.auth import get_user_model

from apps.base.base_model import BaseModel
from category.models import Category

User = get_user_model()



class Blog(BaseModel):
    user = models.ForeignKey(User, verbose_name='用户', help_text='用户',on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='类别', help_text='类别',on_delete=models.CASCADE)
    content = models.TextField(blank=True, verbose_name='博客正文', help_text='博客正文')
    title = models.TextField(null=False, blank=False, verbose_name="标题", help_text='标题')
    num = models.IntegerField(null=True, blank=True, default=0, verbose_name='数量', help_text='数量')

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name

