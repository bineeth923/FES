from django.db import models


class Teacher(models.Model):
    teacherName = models.CharField(max_length=50)

    def __str__(self):
        return self.teacherName


class Subject(models.Model):
    subjectName = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher)

    def __str__(self):
        return self.subjectName
