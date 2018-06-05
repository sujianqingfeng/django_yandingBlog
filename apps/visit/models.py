from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now,timedelta

from base.base_model import BaseModel

User = get_user_model()


class VisitManager(models.Manager):
    # def get_query_set(self):
    #     return models.query.QuerySet(self.model,self._db)

    def get_this_day(self):
        start = now().date()
        end = start + timedelta(days=1)
        return self.get_queryset().filter(add_time__range=(start,end))

    def get_yesterday(self):
        end = now().date()
        start = now() - timedelta(days=1)
        return self.get_queryset().filter(add_time__range=(start,end))

class Visit(BaseModel):
    """
    记录访问ip的模型
    """

    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户',help_text='用户')
    ip = models.GenericIPAddressField(null=False,verbose_name='ip',help_text='ip')
    objects = VisitManager()

    class Meta:
        verbose_name = '访问'
        verbose_name_plural = verbose_name
