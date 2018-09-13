# -*- coding: utf-8 -*-
# __author__ = 'ZKL'
# __date__ = '2018/5/5 11:39'

from django import forms
from captcha.fields import CaptchaField


class LoginFrom(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)
    captcha = CaptchaField(required=True, error_messages={'invalid': '验证码不正确!'})


class RegisterFrom(forms.Form):
    email = forms.EmailField(required=True, error_messages={'invalid': '请填写正确的邮箱!'})
    password = forms.CharField(required=True, min_length=6, error_messages={'invalid': '密码不能少于6位!'})
    rePassword = forms.CharField(required=True, min_length=6, error_messages={'invalid': '密码不能少于6位!'})
    captcha = CaptchaField(required=True, error_messages={'invalid': '验证码不正确!'})




















































































