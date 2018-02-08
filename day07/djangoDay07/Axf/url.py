from django.conf.urls import url

from Axf import views
# from djangoDay07.urls import urlpatterns

urlpatterns=[
    url('^hello/', views.hello),
    url('^home/', views.home,name='home'),
    url('^market$', views.market,name='market'),
    url('^market/(?P<typeid>\d+)/', views.marketWithParams,name='marketWithParams'),
    url('^cart/', views.cart, name='cart'),
    url('^mine/', views.mine, name='mine'),

]