from django.db import models
from app.models import UserProfile
from datetime import datetime
from DjangoUeditor.models import UEditorField
# Create your models here.


# 文章标签
class Articletype(models.Model):
    name = models.CharField(null=True, max_length=50, verbose_name='标签名')

    class Meta:
        db_table = 'blog_articletype'
        verbose_name = '博客标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    title = models.CharField(null=True, max_length=255, verbose_name='博客标题')
    content = UEditorField(verbose_name='博客内容', width=600, height=300, toolbars="full", imagePath="media/ueditor/", filePath="media/ueditor/", upload_settings={'imageMaxSize': 1204000}, default='')
    publish_time = models.DateTimeField(default=datetime.now, null=True, verbose_name='发布时间')
    update_time = models.DateTimeField(default=datetime.now, null=True,verbose_name='更新时间')
    comment_num = models.IntegerField(null=True, verbose_name='评论数')
    keep_num = models.IntegerField(null=False, default='0', verbose_name='收藏数')
    poll_num = models.IntegerField(null=False, default='0', verbose_name='点赞数')
    browse_num = models.IntegerField(null=False, default='0', verbose_name='浏览数')
    article_type = models.IntegerField(null=True)
    author = models.IntegerField(null=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='作者')
    article_type = models.ForeignKey(Articletype, on_delete=models.CASCADE, verbose_name='博客标签')

    class Meta:
        db_table = 'blog_article'
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name


# 评论
class Comment(models.Model):
    content = models.CharField(null=True, max_length=255)
    date = models.DateTimeField(null=True, default=datetime.now)
    article = models.IntegerField(null=True)
    user = models.IntegerField(null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog_comment'
        verbose_name = '评论'
        verbose_name_plural = verbose_name


# 文章用户
class Article_user(models.Model):
    article = models.IntegerField(null=True)
    user = models.IntegerField(null=True)
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog_artivle_user'
        verbose_name = '博客文章用户'
        verbose_name_plural = verbose_name


# 收藏
class Keep(models.Model):
    article = models.IntegerField(null=True)
    user = models.IntegerField(null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog_keep'
        verbose_name = '收藏'
        verbose_name_plural = verbose_name


# 点赞数
class Poll(models.Model):
    article = models.IntegerField(null=True)
    user = models.IntegerField(null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog_poll'
        verbose_name = '点赞'
        verbose_name_plural = verbose_name


