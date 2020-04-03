from django.shortcuts import render
 
def hello(request):
    context          = {}
    context['hello'] = 'This is a question syetem.'
    return render(request, 'hello.html', context)