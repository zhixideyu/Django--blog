# -*- coding: utf-8 -*-
# __author__ = 'ZKL'
# __date__ = '2018/5/19 18:29'


from django import template
import re
# 获取过滤器的集合
register = template.Library()

@register.filter
def strip_ele(value):
    value = re.sub(re.compile(r'<.*?>|&nbsp;', re.S), '', value)[:20]
    if len(value) == 20:
        value += '......'
    return value