# -*- coding: utf-8 -*-
# __author__ = 'ZKL'
# __date__ = '2018/5/19 10:02'
import xadmin
from .models import UserProfile, EmailVerifyRecord
from xadmin.views import CommAdminView, BaseAdminView


# 网页头部导航标题;底部版权;左侧导航折叠筐
class CustomView(object):
    site_title = '笨笨熊后台管理'
    site_footer = '笨笨熊'
    menu_style = 'accordion'


xadmin.site.register(CommAdminView, CustomView)


# 模版主题配置
class ThemeView(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(BaseAdminView, ThemeView)


class EmailAdmin(object):
    list_display = ['email', 'code', 'send_time', 'exprie_time', 'send_type', 'status']
    search_fields = ['email', 'send_type']
    list_filter = ['send_time']


xadmin.site.register(EmailVerifyRecord, EmailAdmin)


