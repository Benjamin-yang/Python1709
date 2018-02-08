from django.db import models

# Create your models here.
class BaseMain(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=32)

    class Meta:
        abstract= True


class MainWheel(BaseMain):

    class Meta:
        db_table='axf_wheel'

class MainNav(BaseMain):

    class Meta:
        db_table='axf_nav'


class MainMustBuy(BaseMain):

    class Meta:
        db_table='axf_mustbuy'

class MainShop(BaseMain):

    class Meta:
        db_table='axf_shop'


# trackid,name,img,categoryid,brandname,img1,childcid1,
# productid1,longname1,price1,marketprice1,img2,childcid2,productid2,longname2,price2,marketprice2,img3,childcid3,productid3,longname3,price3,marketprice3) values("21782","优选水果","http://img01.bqstatic.com//upload

class MainShow(BaseMain):
    categoryid=models.CharField(max_length=32)
    brandname=models.CharField(max_length=100)
    img1=models.CharField(max_length=200)
    childcid1=models.CharField(max_length=32)
    productid1=models.CharField(max_length=32)
    longname1=models.CharField(max_length=200)
    price1=models.CharField(max_length=100)
    marketprice1=models.CharField(max_length=100)

    img2=models.CharField(max_length=200)
    childcid2=models.CharField(max_length=32)
    productid2=models.CharField(max_length=32)
    longname2=models.CharField(max_length=200)
    price2=models.CharField(max_length=100)
    marketprice2=models.CharField(max_length=100)

    img3=models.CharField(max_length=200)
    childcid3=models.CharField(max_length=32)
    productid3=models.CharField(max_length=32)
    longname3=models.CharField(max_length=200)
    price3=models.CharField(max_length=100)
    marketprice3=models.CharField(max_length=100)


    class Meta:
        db_table='axf_mainshow'

# axf_foodtypes(typeid,typename,childtypenames,typesort)
class FoodType(models.Model):
    typeid = models.CharField(max_length=32)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.CharField(max_length=32)

    class Meta:
        db_table='axf_foodtypes'


# productid,productimg,productname,productlongname,isxf,
# pmdesc,specifics,price,marketpriprice,categoryid,
# childcid,childcidname,dealerid,storenums,productnum
class Goods(models.Model):
    productid=models.CharField(max_length=32)
    productimg=models.CharField(max_length=200)
    productname=models.CharField(max_length=100)
    productlongname=models.CharField(max_length=200)
    isxf=models.BooleanField(default=False)
    pmdesc=models.CharField(max_length=100)
    specifics=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    marketprice=models.CharField(max_length=100)
    categoryid=models.CharField(max_length=100)
    childcid=models.CharField(max_length=100)
    childcidname=models.CharField(max_length=100)
    dealerid=models.CharField(max_length=100)
    storenums=models.CharField(max_length=100)
    productnum=models.CharField(max_length=100)

    class Meta:
        db_table='axf_goods'
