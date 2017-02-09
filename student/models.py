from django.db import models


class Student:
    studentName = models.CharField(max_length=150)
    rollNo = models.IntegerField

    def __str__(self):
        return self.studentName
