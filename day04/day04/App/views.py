from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    # return HttpResponse('hello sss')
    resp= HttpResponse('hello')
    resp.write('  Game')
    resp.flush()
    return resp