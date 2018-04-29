from django.db import models
from django.contrib.auth import get_user_model


from apps.base.base_model import BaseModel


User = get_user_model()

class About(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    content = models.CharField(max_length=10000,null=False,blank=False,verbose_name='内容')



    class Meta:
        verbose_name = "关于"