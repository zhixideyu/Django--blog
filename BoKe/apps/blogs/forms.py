# -*- coding: utf-8 -*-
# __author__ = 'ZKL'
# __date__ = '2018/5/7 22:02'

from django import forms


class CommentForm(forms.Form):
    content = forms.CharField(max_length='200', required=True, error_messages={'invalid': '内容超过范围200字!'})


