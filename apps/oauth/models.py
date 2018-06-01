from django.db import models
from user.models import User

# 用户登录的类型
type = (
    ('1', 'github'),
    ('2', 'qq'),
    ('3', 'weibo')
)


class OAuth(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    openid = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=1, choices=type)

    class Meta:
        verbose_name = '认证'
        verbose_name_plural = verbose_name
