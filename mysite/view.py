from django.shortcuts import render

def hello(request):
    context          = {}
    context['hello'] = '点击进入问卷系统'
    context['admin'] = '点击进入管理页面'
    return render(request, 'hello.html', context)