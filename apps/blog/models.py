from django.db import models

from apps.base.base_model import BaseModel


# Create your models here.

class Blog(BaseModel):
    content = models.TextField(blank=True, verbose_name='博客正文')

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客'
