from django.shortcuts import render, redirect
from .models import Article, Articletype, Comment, Poll, Keep
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import CommentForm
from django.contrib.auth.views import login_required
# Create your views here.


# 首页
def index(request):
    # 展示所有数据
    sx_id = request.GET.get('sx_id')
    time = request.GET.get('time')
    comment = request.GET.get('comment')
    if sx_id:
        infos = Article.objects.all().order_by('-keep_num')
    elif time:
        infos = Article.objects.all().order_by('-publish_time')
    elif comment:
        infos = Article.objects.all().order_by('-comment_num')
    else:
        infos = Article.objects.all().order_by('-publish_time')
    paginator = Paginator(infos, 10)
    page_num = request.GET.get('page', '1')
    try:
        page_info = paginator.page(page_num)
    except PageNotAnInteger as e:
        page_info = paginator.page(1)
    except EmptyPage as e:
        if int(page_num) > paginator.num_pages:
            page_info = paginator.page(paginator.num_pages)
        else:
            page_info = paginator.page(1)
    return render(request, 'homepage.html', {'paginator': paginator, 'page_info': page_info})


# 添加文章
@login_required
def add(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'add-article.html')
        else:
            return render(request, 'article.html', {'error': '请先登录, 在操作!'})
    elif request.method == 'POST':
        author_id = request.POST.get('author_id', '')
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        type = request.POST.get('type', '')
        # 保存博客的类型
        a = Articletype(name=type)
        a.save()
        p = Article(title=title, content=content, author_id=author_id, article_type_id=a.id)
        p.save()
        return redirect('/show/?article_id={}'.format(p.id))


# 展示文章
def show(request):
    if request.method == 'GET':
        form = CommentForm()
        article_id = request.GET.get('article_id', '')
        poll = Poll.objects.filter(article_id=article_id, user_id=request.user.id)
        if poll:
            is_poll = True
        else:
            is_poll = False
        keep = Keep.objects.filter(article_id=article_id, user_id=request.user.id)
        if keep:
            is_keep = True
        else:
            is_keep = False
        info = Article.objects.get(id=article_id)
        # 评论内容
        infos = info.comment_set.all()
        paginator = Paginator(infos, 4)
        page_num = request.GET.get('page', '1')
        try:
            page_info = paginator.page(page_num)
        except PageNotAnInteger as e:
            page_info = paginator.page(1)
        except EmptyPage as e:
            if int(page_num) > paginator.num_pages:
                page_info = paginator.page(paginator.num_pages)
            else:
                page_info = paginator.page(1)
        # 评论数
        num = Comment.objects.filter(article_id=article_id)
        return render(request, 'article.html', {'info': info, 'num': len(num), 'form': form, 'page_info': page_info, 'article_id':article_id, 'is_poll': is_poll, 'is_keep': is_keep})
    elif request.method == 'POST':
        pass


# 个人中心
@login_required
def user(request):
    # 接作者的id
    author_id = request.GET.get('author_id', '')
    if author_id:
        # 根据作者id查询出所有的它对应的文章
        infos = Article.objects.filter(author_id=author_id)
        my_article = len(infos)
        keep_num = Keep.objects.filter(user_id=request.user.id)
        keep_num = len(keep_num)
        paginator = Paginator(infos, 4)
        page_num = request.GET.get('page', '1')
        try:
            page_info = paginator.page(page_num)
        except PageNotAnInteger as e:
            page_info = paginator.page(1)
        except EmptyPage as e:
            if int(page_num) > paginator.num_pages:
                page_info = paginator.page(paginator.num_pages)
            else:
                page_info = paginator.page(1)
        # 收藏的文章
        info_list = Keep.objects.filter(user_id=author_id)
        paginator = Paginator(info_list, 4)
        collect_page_num = request.GET.get('collect_page', '1')
        try:
            keep_info = paginator.page(collect_page_num)
        except PageNotAnInteger as e:
            keep_info = paginator.page(1)
        except EmptyPage as e:
            if int(collect_page_num) > paginator.num_pages:
                keep_info = paginator.page(paginator.num_pages)
            else:
                keep_info = paginator.page(1)
        # 评论过的文章
        comment_info_list = Comment.objects.filter(user_id=author_id)
        comment_info = Paginator(comment_info_list, 4)
        comment_page_num = request.GET.get('comment_page', '1')
        try:
            comment_info = comment_info.page(comment_page_num)
        except PageNotAnInteger as e:
            comment_info = comment_info.page(1)
        except EmptyPage as e:
            if int(collect_page_num) > comment_info.num_pages:
                comment_info = comment_info.page(comment_info.num_pages)
            else:
                comment_info = comment_info.page(1)

        return render(request, 'users.html', {'page_info': page_info, 'keep_info': keep_info, 'comment_info': comment_info})
    else:
        return redirect('/')


# 点赞
@login_required
def poll(request):
    article_id = request.GET.get('article_id', '')
    poll = Poll.objects.filter(article_id=article_id, user_id=request.user.id)
    # poll不存在, 执行点赞操作
    if not poll:
        p = Poll(article_id=article_id, user_id=request.user.id)
        p.save()
        p_num = p.article.poll_num
        p_num += 1
        p.article.poll_num = p_num
        p.article.save()
    else:
        poll.delete()
        article = Article.objects.get(id=article_id)
        a_num = article.poll_num
        a_num -= 1
        article.poll_num = a_num
        article.save()
    return redirect('/show/?article_id={}'.format(article_id))


# 收藏
@login_required
def keep(request):
    article_id = request.GET.get('article_id', '')
    if request.user.is_authenticated:
        user_id = request.user.id
    else:
        return render(request, 'article.html')
    article = Article.objects.get(id=article_id)
    if len(Keep.objects.filter(article_id=article_id, user_id=user_id)) >= 1:
        article.keep_num = article.keep_num - 1
        article.save()
        Keep.objects.filter(user_id=user_id).delete()
    else:
        Keep.objects.create(article_id=article_id, user_id=user_id)
        info_list = Keep.objects.filter(article_id=article_id)
        article.keep_num = len(info_list)
        article.save()
    return redirect('/show/?article_id={}'.format(article_id))


# 评论
@login_required
def comment(request):
    info = CommentForm(request.POST)
    if info.is_valid():
        content = info.cleaned_data['content']
        user_id = request.user.id
        article_id = request.GET.get('article_id')
        c = Comment(content=content, user_id=user_id, article_id=article_id)
        c.save()
        comment_num_list = Comment.objects.filter(article_id=article_id)
        article = Article.objects.get(id=article_id)
        article.comment_num = len(comment_num_list)
        article.save()
        return redirect('/show/?article_id={}'.format(article_id))
    else:
        return render(request, {'info': info})


# 修改个人资料
def update(request):
    return render(request, 'update_data.html')


# 后台
