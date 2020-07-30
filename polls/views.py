from django.shortcuts import render

from django.urls import reverse

from django.http import HttpResponse

# Create your views here.

def index(request):
    print(reverse('index'))
    return HttpResponse("Hello, world. You're at the polls index.")

def index_with_parameter(request, year, month):
    print(reverse('index_with_parameter', kwargs={'year':2020, 'month':7}))
    return HttpResponse('This is view response {0}, {1}'.format(year,month))

def login_page(request):
    from django.template import loader
    # 加载模版
    safe_string = loader.get_template('login.html')
    # 渲染模版
    res = safe_string.render()
    return HttpResponse(res)

    # 直接使用 render()
    # res = render(request, 'login.html')

    # return res
def validate(request):
    username = request.POST['username']
    password = request.POST['password']

    c = {}
    c['username'] = username

    if username == 'admin' and password == '123456':
        return render(request, 'welcome.html', context=c)
    else:
        raise Exception('用户名或密码错误!')



