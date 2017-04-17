from django.db import models

from teacher.models import Teacher, Semester


class Survey(models.Model):
    surveyName = models.CharField(max_length=150)
    sem = models.ForeignKey(Semester)

    def __str__(self):
        return self.surveyName


class Form(models.Model):
    formName = models.CharField(max_length=150)
    teacher = models.ForeignKey(Teacher)
    semester = models.ForeignKey(Semester)
    survey = models.ForeignKey(Survey)
    def __str__(self):
        return self.formName


class Token(models.Model):
    tokenId = models.CharField(max_length=6)
    form = models.ForeignKey(Form, null=True)
    survey = models.ForeignKey(Survey, null=True)

    def __str__(self):
        return self.tokenId


class MCQ(models.Model):
    textName = models.CharField(max_length=200)
    form = models.ForeignKey(Form)
    token = models.ForeignKey(Token, null=True)

    def __str__(self):
        return self.textName


class Options(models.Model):
    textName = models.CharField(max_length=200)
    result = models.IntegerField(default=0)
    mcq = models.ForeignKey(MCQ)
    form = models.ForeignKey(Form)

    def __str__(self):
        return self.textName


class TextView(models.Model):
    textName = models.CharField(max_length=200)
    result = models.CharField(max_length=200)
    form = models.ForeignKey(Form)
    token = models.ForeignKey(Token, null=True)

    def __str__(self):
        return self.textName
