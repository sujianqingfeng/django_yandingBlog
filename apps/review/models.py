from django.db import models
from django.contrib.auth import get_user_model
from django_comments.abstracts import CommentAbstractModel
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.contenttypes.models import ContentType

from apps.base.base_model import BaseModel


User = get_user_model()


class Review(MPTTModel, CommentAbstractModel):
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='上级回复',
                            related_name='children')

    def descendants(self):
        """
        获取回复的全部子孙回复，按回复时间正序排序
        """
        return self.get_descendants().order_by('submit_date')

    def descendants_count(self):
        return self.get_descendant_count()

    @property
    def ctype(self):
        return ContentType.objects.get_for_model(self)

    @property
    def ctype_id(self):
        return self.ctype.id

    class Meta(CommentAbstractModel.Meta):
        verbose_name = "评论"
        verbose_name_plural = verbose_name
