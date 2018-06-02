from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth import get_user_model
import markdown
from django.utils.html import strip_tags

from apps.base.base_model import BaseModel
from category.models import Category
from review.models import Review

User = get_user_model()


class Blog(BaseModel):
    user = models.ForeignKey(User, verbose_name='用户', help_text='用户', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='类别', help_text='类别', on_delete=models.CASCADE)
    content = models.TextField(blank=True, verbose_name='博客正文', help_text='博客正文')
    title = models.TextField(null=False, blank=False, verbose_name="标题", help_text='标题')
    num = models.IntegerField(null=True, blank=True, default=0, verbose_name='数量', help_text='数量')
    pinned = models.BooleanField(default=False, verbose_name='置顶', help_text='置顶')
    review = GenericRelation(Review, object_id_field='object_pk', content_type_field='content_type', verbose_name='评论')
    excerpt = models.CharField(max_length=200, blank=True, verbose_name='摘要', help_text='摘要')

    def save(self, *args, **kwargs):
        """
        覆写save方法，设置摘要   通过信号应该也可以
        """
        if not self.excerpt:
            md = markdown.Markdown(extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite'])
            self.excerpt = strip_tags(md.convert(self.content))[:54]
        super(Blog, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name
