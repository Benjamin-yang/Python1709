import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import UserModel


def hello(request):
    return HttpResponse('hello work')


def index(request):
    return render(request, 'index.html')


def cart(request):
    # 判断是否还有优惠券，是否抢到
    num = random.randrange(1, 200)
    if num > 190:
        return HttpResponse('抢到了')
    return HttpResponse('下次再来')
    # return None


#
#
def bug(request):
    num = 1 / 0
    return HttpResponse('bug')


def doUpload(request):
    username = request.POST.get('username')
    icon = request.FILES['icon']
    u = UserModel()
    u.u_name = username
    u.u_icon = icon
    u.save()
    return HttpResponse('上传成功')


def upload(request):
    return render(request,'UserUpload.html')
