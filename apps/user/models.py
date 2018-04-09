from _datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    '''
    用户
    '''

    SEX_TYPE = (
        (1, '男'),
        (2, '女'),
        (3, '未知')
    )

    birthday = models.DateField(null=True, blank=True, verbose_name='出生年月', help_text='出生年月')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间', help_text='添加时间')
    update_time = models.DateField(default=datetime.now, verbose_name='更新时间', help_text='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除', help_text='是否删除')
    sex = models.IntegerField(choices=SEX_TYPE, default=3, verbose_name='性别', help_text='性别: 1(男),2(女),3(未知)')
    phone = models.CharField(null=True, blank=True, max_length=11, verbose_name="手机", help_text='手机')
    icon = models.ImageField(upload_to='static/images/%Y/%m/%d', null=True, blank=True, verbose_name="头像",
                             help_text='头像')
    desc = models.CharField(null=True, blank=True, default='', max_length=100, verbose_name="描述", help_text='描述')
    github = models.CharField(null=True, blank=True, default='', max_length=100, verbose_name="github",
                              help_text='github')
    other_link = models.CharField(null=True, blank=True, default='', max_length=100, verbose_name="其他链接",
                                  help_text='其他链接')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.username
