# -*- coding: utf-8 -*-
# __author__ = 'ZKL'
# __date__ = '2018/5/5 15:20'
from django.core.mail import send_mail
from app.models import EmailVerifyRecord
import random
from datetime import datetime
import datetime
from BoKe import settings


# 随机产生验证码
def random_captcha():
    string = 'qwertyuioplkjhgfASDFZXCVBNMPLMOKN'
    captcha = ''
    for x in range(16):
        captcha += random.choice(string)
    return captcha


# 发送邮件
def send_eamil(to_email, send_type='register'):
    eamil = EmailVerifyRecord()
    eamil.email = to_email
    eamil.code = random_captcha()
    eamil.exprie_time = datetime.datetime.now() + datetime.timedelta(days=7)
    eamil.send_type = send_type
    try:
        title = ''
        content = ''
        if send_type == 'register':
            title = '笨笨熊博客激活邮件'
            content = '欢迎注册笨笨熊博客, 点击链接激活您的账户:<a href="http://127.0.0.1:8000/app/active/{}">127.0.0.1:8000/app/active/{}</a>'.format(eamil.code, eamil.code)
        else:
            title = '笨笨熊博客密码找回邮件'
            content = ''
        res = send_mail(title, '', settings.EMAIL_HOST_USER, [to_email], html_message=content)
        if res == 1:
            eamil.save()
            return True
        else:
            return False
    except Exception as e:
        return False

