from django.conf.urls import url

from homework import views

urlpatterns = [
    # url(r'^hello',views.hello),
    # url(r'^addstudents/',views.addStudents),
    # url(r'^getstudents/(?P<page_num>\d+)/',views.getStudents,name="getStudents"),
    url(r'^getverifycode/',views.getVerifyCode,name='getVerifyCode'),
    url(r'^dologin/',views.doLogin,name="doLogin"),
    url(r'^login/',views.login,name="login"),
]
