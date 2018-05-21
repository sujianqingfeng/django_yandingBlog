from django.db import models
from django.contrib.auth import get_user_model


from apps.base.base_model import BaseModel


User = get_user_model()

class Friend(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='用户')
    icon = models.ImageField(upload_to='static/images/%Y/%m/%d',default='', null=False, blank=False, verbose_name='图片url')

    title = models.CharField(max_length=100,null=False,blank=False,verbose_name='题目')
    link = models.CharField(max_length=100,null=False,blank=False,verbose_name='链接')
    desc = models.CharField(max_length=100,null=False,blank=False,verbose_name='描述')



    class Meta:
        verbose_name = "友链"