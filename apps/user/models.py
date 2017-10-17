from _datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    '''
    用户
    '''
    birthday = models.DateField(null=True, blank=True, verbose_name='出生年月')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')
    update_time = models.DateField(default=datetime.now, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False,verbose_name='是否删除')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.username
