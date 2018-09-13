# -*- coding: utf-8 -*-
# __author__ = 'ZKL'
# __date__ = '2018/5/19 10:18'
import xadmin
from .models import Article, Articletype


class ArticleAdmin(object):
    list_display = ['author', 'title', 'publish_time', 'update_time', 'comment_num', 'keep_num', 'poll_num', 'browse_num', 'article_type']
    search_fields = ['author', 'title', 'publish_time', 'article_type']
    list_filter = ['publish_time']
    readonly_fields = ['comment_num', 'keep_num','poll_num', 'browse_num']
    # 富文本的插件效果
    style_fields = {'content': 'ueditor'}


xadmin.site.register(Article, ArticleAdmin)


class ArticletypeAdmin(object):
    list_display = ['id', 'name']


xadmin.site.register(Articletype,  ArticletypeAdmin)


