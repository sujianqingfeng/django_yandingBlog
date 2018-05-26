from django.db import models
from django.contrib.auth import get_user_model
from django_comments.abstracts import CommentAbstractModel
from mptt.models import MPTTModel, TreeForeignKey

from apps.base.base_model import BaseModel


User = get_user_model()


class Review(MPTTModel, CommentAbstractModel):
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='上级回复',
                            related_name='children')

    class Meta(CommentAbstractModel.Meta):
        verbose_name = "评论"
        verbose_name_plural = verbose_name
