from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    resp= HttpResponse('hello')
    resp.write('qqGame')
    resp.flush()
    return resp


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def dologin(request):
    username = request.POST.get('username', '游客')
    resp = HttpResponse('u')

    return resp


def logout(request):
    resp = HttpResponse('退出')
    resp.delete_cookie('username')
    return resp