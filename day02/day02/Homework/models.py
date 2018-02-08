from django.db import models


# Create your models here.
class Grade(models.Model):
    g_name = models.CharField(max_length=16, unique=True)
    # 0 python 1 jave 2php 3 html
    g_type = models.IntegerField(default=0)


class Student(models.Model):
    s_num = models.IntegerField(unique=True)
    s_name = models.CharField(max_length=16)

    s_sex = models.NullBooleanField(default=False)
    s_grade = models.ForeignKey(Grade, on_delete=models.PROTECT)
