from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=20, verbose_name='昵称', default='')
    birthday = models.DateTimeField(verbose_name='生日', null=True, blank=True)
    address = models.CharField(max_length=50, verbose_name='住址', default='')
    mobile = models.CharField(max_length=11, verbose_name='手机号', default='')
    image = models.ImageField(upload_to='images/%Y/%m', default='', verbose_name='头像')

    class Meta:
        db_table = 'users'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='用户邮箱')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')
    exprie_time = models.DateTimeField(null=True, verbose_name='过期时间')
    send_type = models.CharField(choices=(('register', '注册邮件'), ('forget', '找回密码')), max_length=10, verbose_name='邮件类型')
    status = models.BooleanField(choices=((True, '已使用'), (False, '未使用')), verbose_name='邮件状态', default=False)

    class Meta:
        verbose_name = '邮箱验证'
        verbose_name_plural = verbose_name
