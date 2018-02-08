from django.conf.urls import url

from App import views

urlpatterns = [
    url('^hello/',views.hello),
    url('^home/',views.home, name='home'),
    url('^market/',views.market, name='market'),
    url('^cart/',views.cart, name='cart'),
    url('^mine/',views.mine, name='mine'),
]
