from django.http import HttpResponse
from django.shortcuts import render


# 创建index页面
def index_view(request):
    # 向模板层传递的参数
    parameter = {
        'server_name': 'DAS'
    }

    # 使用模板创建页面
    return render(request, 'index.html', parameter)


# 创建djang图片展示页面
def show_django_image_view(request):
    # 使用模板创建页面
    return render(request, 'djangoDemo/django.html')
