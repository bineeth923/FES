from django.contrib import admin
from django.db import models
from random import Random
from django.utils import timezone
import string

class MCQ(models.Model):
    text = models.CharField(max_length=200)
    position = models.IntegerField

    def __str__(self):
        return self.text


class Options(models.Model):
    mcq = models.ForeignKey(MCQ)
    text = models.CharField(max_length=100)
    select = models.BooleanField(default=False)


class Students(models.Model):
    user_name = models.CharField(max_length=50)
    date_created = models.DateField
    group = models.ForeignKey(Targeted_Class)

    def __str__(self):
        return self.user_name
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateField
    group = models.ForeignKey(Targeted_Class)


class Targeted_Class:
    name = models.CharField(max_length=50)
    date_created = models.DateField

