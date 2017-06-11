from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.http import HttpResponse
from survey import models as survey_model
from teacher import models as teacher_model
from functions import *


@login_required
@user_passes_test(is_teacher)
def index(request):
    print(request.user.username)
    teacher = teacher_model.Teacher.objects.get(teacherName = request.user.username)
    semesters = survey_model.Semester.objects.filter(teacher = teacher)
    primaryKey = []
    for semester in semesters:
        primaryKey.append(semester.pk)
    zipped_data = zip(semesters , primaryKey)
    context = {
        'zippedData' : zipped_data
    }
    return render(request , 'teacher/index.html' , context)

def forms(request , sem):
    teacher = teacher_model.Teacher.objects.get(teacherName=request.user.username)
    semester = survey_model.Semester.objects.get(pk=int(sem))
    all_forms = survey_model.Form.objects.filter(semester=semester)
    forms = all_forms.filter(teacher=teacher)
    primaryKey=[]
    for form in forms:
        primaryKey.append(form.pk)
        print(form.formName + ':' + str(form.pk))
    zipped_data = zip(forms , primaryKey)
    context = {
        'zipped_data' : zipped_data
    }
    return render(request , 'teacher/forms.html' , context)

def result(request ,sem ,  formId):
    form = survey_model.Form.objects.get(pk=int(formId))
    allToken = survey_model.Token.objects.filter(form = form)
    mcqs = survey_model.MCQ.objects.filter(form=form).filter(token__isnull=True)
    textViews = survey_model.TextView.objects.filter(form=form).filter(token__isnull=True)
    mcq_questions = []
    for mcq in mcqs:
        options = (survey_model.Options.objects.filter(mcq=mcq)).filter(form = form)
        mcq_questions.append([mcq.textName, options])
    context = {
        'mcq_questions': mcq_questions,
        'text_view_questions': textViews,
        'subject' : form.teacher.subject.subjectName,
        'sem' : form.semester.semesterName,
        'count' : allToken.count
    }
    return render(request , 'teacher/result.html' , context)