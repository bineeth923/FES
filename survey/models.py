from django.db import models


class survey:
    surveyName = models.CharField(max_length=150)
    dateCreated = models.DateField
    dateEnded = models.DateField

    def __str__(self):
        return self.surveyName


class Form:
    formName = models.CharField(max_length=150)

    def __str__(self):
        return self.formName


class MCQ:
    textName = models.CharField(max_length=200)
    form = models.ForeignKey(Form)

    def __str__(self):
        return self.textName


class Options:
    textName = models.CharField(max_length=200)
    result = models.BooleanField
    mcq = models.ForeignKey(MCQ)

    def __str__(self):
        return self.textName


class TextView:
    textName = models.CharField(max_length=200)
    result = models.CharField(max_length=200)
    form = models.ForeignKey(Form)

    def __str__(self):
        return self.textName


class Token:
    form = models.ForeignKey(Form)
    tokenId = models.IntegerField

    def __str__(self):
        return self.tokenId
