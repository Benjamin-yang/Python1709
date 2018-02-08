from django.conf.urls import url

from App import views

urlpatterns = [
    url('^hello/', views.hello),
    url('^index/', views.index, name='index'),
    url(r'^cart/', views.cart),
    url(r'bug/', views.bug),
    url(r'^doupload/', views.doUpload, 'name=doUpload'),
    url(r'^upload/', views.upload, 'name=upload'),

]
