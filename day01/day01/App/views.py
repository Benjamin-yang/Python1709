import random

from django.db.models import F, Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views he= re.
from App.models import Grade, Student


def hello(request):
    return HttpResponse('hello world')


def addGrade(request):
    grade = Grade()
    grade_num = random.randrange(1, 500)
    grade.g_name = 'python18%d' % grade_num
    grade.g_girl_num = grade_num
    grade.save()
    return HttpResponse('Add Success %d' % grade_num)


def getGrades(request):
    # grades = Grade.objects.filter(g_girl_num__gt=F('g_boy_num'))
    # grades = Grade.objects.filter(g_girl_num__gt=30).filter(g_boy_num__gt=20)
    grades = Grade.objects.filter(Q(g_boy_num__gt=22)&Q(g_girl_num__gt=30))
    data = {
        'grades': grades,

    }

    return render(request, 'Gradelist.html', context=data)



def addStudent(request):
    stu = Student()
    name_num = random.randrange(1,200)
    stu.s_name = '小明%d' % name_num
    stu.s_age = name_num
    grade = Grade.objects.last()
    stu.s_grade = grade
    stu.save()
    return HttpResponse('添加学生%d' % name_num)



def getStudents(request):
    grade = Grade.objects.last()
    # stu = Student()
    # grades = Grade.objects.filter(g_girl_num__gt=F('g_boy_num'))
    # grades = Grade.objects.filter(g_girl_num__gt=30).filter(g_boy_num__gt=20)
    # students = Student.objects.filter())
    students = grade.student_set.all()

    data = {
        'students': students,

    }

    return render(request, 'StudentList.html', context=data)
