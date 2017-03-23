from django.db import models


class Subject(models.Model):
    subjectName = models.CharField(max_length=100)




class Teacher(models.Model):
    teacherName = models.CharField(max_length=50)
    Semester = models.CharField(max_length=2)
    subject = models.ForeignKey(Subject)

    def __str__(self):
        return self.teacherName
