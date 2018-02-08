from django.conf.urls import url

from Homework import views

urlpatterns=[
    url(r'hello/', views.hello),
    url(r'^getgradelist/',views.getGradeList, name='getGradeList'),
    url(r'^getstudentlist/(?P<gradeid>\d+)/',views.getStudentList, name='getStudentList'),
]