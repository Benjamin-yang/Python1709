from django.conf.urls import url

from Two import views

urlpatterns=[
    url('^addstudents/',views.addStudent),
]