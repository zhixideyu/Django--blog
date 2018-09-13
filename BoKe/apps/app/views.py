from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterFrom, LoginFrom
from .models import UserProfile, EmailVerifyRecord
from django.contrib.auth.hashers import make_password
from utils.email_utils import send_eamil
from django.contrib.auth import logout, login
from datetime import datetime
import time
from django.contrib.auth import authenticate
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

# Create your views here.


# 登录
def logins(request):
    if request.method == 'GET':
        form = LoginFrom()
        return render(request, 'login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginFrom(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request=request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'form': form, 'error': '账号或密码错误, 请检查后重新登录!'})
        else:
            return render(request, 'login.html', {'form': form})


# 自定义验证
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(email=username) | Q(mobile=username)| Q(username=username))
            if user.check_password(password):
                return user
            else:
                return None
        except Exception as e:
            return None


# 注册
def register(request):
    if request.method == 'GET':
        form = RegisterFrom()
        return render(request, 'register.html', {'form': form})
    elif request.method == 'POST':
        form = RegisterFrom(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            rePassword = form.cleaned_data['rePassword']
            if password != rePassword:
                return render(request, 'register.html', {'form': form, 'error': '两次密码不一致!'})
            if UserProfile.objects.filter(email=email):
                return render(request, 'register.html', {'form': form, 'mistake': '邮箱已存在, 请重新注册!'})
            user = UserProfile(email=email, password=make_password(password))
            user.is_active = 1
            # 后台权限
            user.is_staff = 0
            # 保存邮箱, 来登录后台
            user.username = email
            user.save()
            if send_eamil(email, send_type='register'):
                return HttpResponse('笨笨熊博客网! 恭喜您注册成功, 激活邮件已发送至您的邮箱, 请注意查收!')
            else:
                return HttpResponse('笨笨熊博客网! 恭喜您注册成功, 激活邮件发送失败, 请检查后重试或者联系客服!')
        else:
            return render(request, 'register.html', {'form': form})


# 激活账户
def active(request, code):
    emailRecord = EmailVerifyRecord.objects.filter(code=code)
    if emailRecord:
        emailRecord = emailRecord[0]
        if emailRecord.status:
            return HttpResponse('该验证连接已失效! 请重新注册!')
        now = datetime.now()
        now_time = time.mktime(now.timetuple())
        exprie_time = time.mktime(emailRecord.exprie_time.timetuple())
        if now_time > exprie_time:
            return HttpResponse('激活邮件已失效!')
        user = UserProfile.objects.get(email=emailRecord.email)
        user.is_active = 1
        user.save()
        emailRecord.status = True
        emailRecord.save()
        return HttpResponse('<a href="http://127.0.0.1:8000/app/login/">您的账号{}已激活成功, 点击登录</a>'.format(user.email))
    else:
        return HttpResponse('您访问的激活链接不存在, 请检查后重新访问!')


# 注销
def log_out(request):
    logout(request)
    return redirect('/')