from django.db import models
from django.contrib.auth import get_user_model


from apps.base.base_model import BaseModel
from blog.models import Blog

User = get_user_model()

class Review(BaseModel):
    user = models.ForeignKey(User, verbose_name='用户')
    blog = models.ForeignKey(Blog,verbose_name='博客')
    content = models.CharField(max_length=700,null=False,blank=False,verbose_name='评论内容')



    class Meta:
        verbose_name = "评论"
