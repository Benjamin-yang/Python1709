from django.conf.urls import url

from App import views

urlpatterns=[
    url(r'hello/', views.hello),
    url(r'^addgrade', views.addGrade),
    url(r'^getgrades/', views.getGrades),
    url(r'addstudent/', views.addStudent),
    url(r'getstudents/',views.getStudents),
]