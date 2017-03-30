from django.db import models
from survey.models import Survey


class admin(models.Model):
    adminName = models.CharField(max_length=50)


class UserGroup(models.Model):
    userGroupName = models.CharField(max_length=50)
    survey = models.ForeignKey(Survey)