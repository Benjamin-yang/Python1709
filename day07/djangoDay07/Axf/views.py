from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from Axf.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow, FoodType, Goods


def hello(request):
    return HttpResponse('hello')


def home(request):
    wheels = MainWheel.objects.all()
    navs = MainNav.objects.all()
    mustbuys = MainMustBuy.objects.all()
    mainshops = MainShop.objects.all()
    mainshops0 = mainshops[0]
    mainshops1_2 = mainshops[1:3]
    mainshops3_6 = mainshops[3:7]
    mainshops7_10 = mainshops[7:11]
    mainshows = MainShow.objects.all()

    data = {
        'title': '首页',
        'wheels': wheels,
        'navs': navs,
        'mustbuys': mustbuys,
        'mainshops0': mainshops0,
        'mainshops1_2': mainshops1_2,
        'mainshops3_6': mainshops3_6,
        'mainshops7_10': mainshops7_10,
        'mainshows': mainshows,
    }
    return render(request, 'app/home/home.html', context=data)

def market(request):
    return redirect(reverse('axf:marketWithParams', kwargs={"typeid":"104749"}))


def marketWithParams(request, typeid):
    foodtypes = FoodType.objects.all()
    # goodslist = Goods.objects.all()[0:21]
    # 商品通过左侧菜单进项分类
    goodslist = Goods.objects.filter(categoryid=typeid)
    # 通过上面两项进一步赛选
    foodtype=foodtypes.filter(typeid=typeid).first()
    # foodtype.childtypenames
    data = {
        'title': '闪购',
        'foodtypes': foodtypes,
        'goodslist': goodslist,

    }
    return render(request, 'app/market/market.html', context=data)



def cart(request):
    data = {
        'title': '购物车',

    }
    return render(request, 'app/cart/cart.html', context=data)


def mine(request):
    data = {
        'title': '  我的',

    }
    return render(request, 'app/mine/mine.html', context=data)
