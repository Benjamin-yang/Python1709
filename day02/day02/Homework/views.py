from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Homework.models import Grade


def hello(request):
    return HttpResponse('hello django')


def getGradeList(request):
    gradelist = Grade.objects.all()
    data = {
        'grades': gradelist,
    }
    return render(request, 'GradeList.html', context=data)


def getStudentList(request,gradeid):
    grades = Grade.objects.filter(pk=gradeid)
    if grades.exists():
        # grades = Grade
        students = grades.student_set_all()
    data={
        'students':students,
    }
    return render(request, 'StudentList.html', context=data)

