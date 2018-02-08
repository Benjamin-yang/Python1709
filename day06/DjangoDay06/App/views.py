from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import MainWheel


def hello(request):
    return HttpResponse('hello 2018/2/1')


def home(request):
    wheels = MainWheel.objects.all()
    data = {
        'title': '首页',
        'wheels': wheels,
    }
    return render(request, 'app/home/home.html', context=data)


def market(request):
    return render(request, 'app/market/market.html',context=market)


def cart(request):
    return render(request, 'app/cart/cart.html', context=cart)


def mine(request):
    return render(request, 'app/mine/mine.html', context=cart)
