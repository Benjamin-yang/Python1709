import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Two.models import Student


def addStudent(request):
    for i in range(1,86):
         s = Student()
         s.s_name = 'jack%d' % random.randrange(1,1000)
         s.save()
         return HttpResponse('s')