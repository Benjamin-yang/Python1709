from django.db import models


# Create your models here.
class BaseMain(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=200)

    trackid = models.CharField(max_length=32)

    class Meta:
        abstract = True
#
class MainWheel(BaseMain):

    class Meta:
        db_table = 'axf_wheel'


class MainNav(BaseMain):

    class Meta:
        db_table = 'axf_nav'
