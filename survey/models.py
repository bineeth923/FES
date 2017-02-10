from django.db import models

from teacher.models import Teacher


class FormLayout(models.Model):
    layoutName = models.CharField(max_length=50)
    layout = models.CharField(max_length=5000)


class Survey(models.Model):
    surveyName = models.CharField(max_length=150)
    dateCreated = models.DateField
    dateEnded = models.DateField
    formLayout = models.ForeignKey(FormLayout)

    def __str__(self):
        return self.surveyName


class Form(models.Model):
    formName = models.CharField(max_length=150)

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


class links(models.Model):
    formLayout = models.ForeignKey(FormLayout)
    teacher = models.ForeignKey(Teacher)
