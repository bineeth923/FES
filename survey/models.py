from django.db import models

from teacher.models import Teacher


class Survey(models.Model):
    surveyName = models.CharField(max_length=150)

    def __str__(self):
        return self.surveyName


class Form(models.Model):
    formName = models.CharField(max_length=150)
    teacher = models.ForeignKey(Teacher)

    def __str__(self):
        return self.formName


class MCQ(models.Model):
    textName = models.CharField(max_length=200)
    form = models.ForeignKey(Form)

    def __str__(self):
        return self.textName


class Options(models.Model):
    textName = models.CharField(max_length=200)
    result = models.BooleanField
    mcq = models.ForeignKey(MCQ)

    def __str__(self):
        return self.textName


class TextView(models.Model):
    textName = models.CharField(max_length=200)
    result = models.CharField(max_length=200)
    form = models.ForeignKey(Form)

    def __str__(self):
        return self.textName


class Token(models.Model):
    form = models.ForeignKey(Form)
    tokenId = models.IntegerField

    def __str__(self):
        return self.tokenId
