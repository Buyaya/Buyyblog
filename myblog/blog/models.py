from django.db import models
from django.contrib.auth.admin import User

# Create your models here.

class Blog_Type(models.Model):
    type_name = models.CharField(max_length=20, verbose_name='博客类型')

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name_plural = '类型'

class Blog(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题')
    context = models.TextField(verbose_name='正文')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='发布人')
    blog_type = models.ForeignKey(Blog_Type, on_delete=models.DO_NOTHING, verbose_name='类型')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最后修改时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '博客'