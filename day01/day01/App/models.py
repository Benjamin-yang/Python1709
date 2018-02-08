from django.db import models


# Create your models here.
class Grade(models.Model):
    g_name = models.CharField(max_length=16, default='Python709')
    g_boy_num = models.IntegerField(default=0)
    g_girl_num = models.IntegerField(default=0)


class Student(models.Model):
    s_name=models.CharField(max_length=16)
    s_age = models.IntegerField(default=18)

    s_sex = models.NullBooleanField(default=False)
    s_grade = models.ForeignKey(Grade)