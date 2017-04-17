from django.db import models


class Subject(models.Model):
    subjectName = models.CharField(max_length=100)

class Semester(models.Model):
    semesterName = models.CharField(max_length=20)


class Teacher(models.Model):
    teacherName = models.CharField(max_length=50)
    Semester = models.ForeignKey(Semester)
    subject = models.ForeignKey(Subject)

    def __str__(self):
        return self.teacherName
