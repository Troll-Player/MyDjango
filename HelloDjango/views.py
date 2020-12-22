# -*- coding:utf-8 -*-
from django.core.paginator import Paginator
from django.shortcuts import render
from HelloDjango.models import Zakernews
from urllib.parse import unquote

# Create your views here.
def index(request):
    return render(request, 'index.html')


def news(request):
    page = int(request.GET.get('page', 1))  # 请求页码
    per_page = int(request.GET.get('per_page', 15))  # 每页展示数据数量

    news_list = Zakernews.objects.all().order_by('id')  # 新闻数量
    paginators = Paginator(news_list, per_page)  # 实例化分页器对象
    page_obj = paginators.page(page)  # 实例化当前页对象
    current_page = page_obj.number  # 当前页码
    num_pages = paginators.num_pages  # 总页数

    left_has_more = False
    right_has_more = False

    if current_page <= 4:
        left_pages = range(1, current_page)
    else:
        left_has_more = True
        left_pages = range(current_page-2, current_page)
    if current_page >= num_pages-3:
        right_pages = range(current_page+1, num_pages+1)
    else:
        right_has_more = True
        right_pages = range(current_page+1, current_page+3)
    if current_page-5 == 0:
        left_jump_pages = 2
    else:
        left_jump_pages = current_page - 5
    if current_page+5 > num_pages:
        right_jump_pages = num_pages - 1
    else:
        right_jump_pages = current_page + 5

    data = {
        'paginators': paginators,
        'page_obj': page_obj,
        'num_pages': num_pages,
        'current_page': current_page,
        'left_has_more': left_has_more,
        'left_pages': left_pages,
        'left_jump_pages': left_jump_pages,
        'right_has_more': right_has_more,
        'right_pages': right_pages,
        'right_jump_pages': right_jump_pages,
    }
    return render(request, 'news.html', context=data)


def detail(request, article_id):
    article_data = Zakernews.objects.get(id=article_id)
    print(article_data)
    article_content = eval(article_data.content)
    data = {
        'article_content': article_content
    }
    return render(request, 'detail.html', context=data)
