from django.http import HttpResponse
from django.shortcuts import render


# 创建index页面
def index_view(request):
    # 向模板层传递的参数
    parameter = {
        'server_name': 'DAS',
    }

    # 使用模板创建页面
    return render(request, 'index.html', parameter)


# 创建djang图片展示页面
def show_django_image_view(request):
    # 向模板层传递的参数
    parameter = {}

    # 使用模板创建页面
    return render(request, 'djangoDemo/django.html', parameter)


# 加减乘除计算器
def add_sub_mul_and_div(request):
    # 判断请求是否为GET请求
    if request.method == 'GET':
        # 判断是否使用GET的方式传递了数值
        if bool(request.GET) is False:
            form = """
            <form action="/calculator/" method="post">
                <p>运算数一: <input type="text" name="a" /></p>
                <p>运算符号: <input type="text" name="operation" /></p>
                <p>运算数二: <input type="text" name="b" /></p>
                <input type="submit" value="Submit" />
            </form>
            """
            return HttpResponse(form)
        else:
            # 判断运算符是否合法
            if request.GET.get('operation') not in ['add', 'sub', 'mul', 'div']:
                return HttpResponse("The input operation is incorrect, please check the operation")
            # 判断运算数是否合法
            elif not (request.GET.get('a').isdigit() and request.GET.get('b').isalnum()):
                return HttpResponse("The input operand is incorrect, please check the operand")
            else:
                # 计算结果并返回
                operations = {'add': '+', 'sub': '-', 'mul': '*', 'div': '/', }
                return HttpResponse(eval(request.GET.get('a') + operations[request.GET.get('operation')] + request.GET.get('b')))
    # 判断请求是否为POST请求
    elif request.method == 'POST':
        # 判断运算符是否合法
        if request.POST.get('operation') not in ['add', 'sub', 'mul', 'div']:
            return HttpResponse("The input operation is incorrect, please check the operation")
        # 判断运算数是否合法
        elif not (request.POST.get('a').isdigit() and request.POST.get('b').isalnum()):
            return HttpResponse("The input operand is incorrect, please check the operand")
        else:
            # 计算结果并返回
            operations = {'add': '+', 'sub': '-', 'mul': '*', 'div': '/', }
            return HttpResponse(eval(request.POST.get('a') + operations[request.POST.get('operation')] + request.POST.get('b')))
    else:
        return HttpResponse("method must be GET or POST, please change your request method")


def mvc_studay(request):
    # 定义一个函数
    def function(words='Ha Ha Ha'):
        return words

    # 定义一个类
    class Animal(object):
        def __init__(self, sound):
            self.sound = sound

        def bark(self):
            return self.sound

    # 向模板层传递的参数, 函数, 类
    parameter = {
        'htmlName': 'mvcStuday.html',
        'function': function,
        'object': Animal(sound='wang ! wang !'),
        'nameList': ['Tom', 'Lily', 'Lucy', 'Piter']
    }

    # 使用模板创建页面
    return render(request, 'mvcStuday.html', parameter)


# 新建计算器
def new_calculator(request):
    if request.method == "GET":
        return render(request, 'calculator.html')
    elif request.method == "POST":
        x = int(request.POST.get('x'))
        y = int(request.POST.get('y'))
        op = request.POST.get('op')

        result = ''
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y

        return render(request, 'calculator.html', locals())
    else:
        return HttpResponse("method must be GET or POST, please change your request method")
