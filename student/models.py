from django.db import models

from administrator.models import UserGroup


class Student(models.Model):
    studentName = models.CharField(max_length=150)
    rollNo = models.IntegerField
    userGroup = models.ForeignKey(UserGroup)

    def __str__(self):
        return self.studentName
