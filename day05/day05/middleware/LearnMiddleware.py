from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


# Mixin多继承

class HelloMiddleware(MiddlewareMixin):
    def process_request(self, request):
            # print(request.path)
            # print(request.META['REMOTE_ADDR'])

        if request.path == '/app/cart/':
            username = request.GET.get('username')
            if username == 'Rock':
                return HttpResponse('恭喜你成为高级会员')

            elif username == 'Tom':
                return HttpResponse('优惠券没了，欢迎下次再来')

    def process_exception(self, request, exception):
        print('异常')
        # 发送异常信息到邮箱
        # 还可以做弥补,
        return redirect(reverse("app:index"))
        # pass
