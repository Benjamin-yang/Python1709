from django.conf.urls import url

from App import views

urlpatterns=[
    url(r'hello/', views.hello),
    url(r'index/', views.index),
    url(r'login/', views.login, name='login'),
    url(r'dologin/', views.dologin),
    url(r'login/', views.login),

    url(r'logout/', views.logout, name='logout'),


]