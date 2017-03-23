from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.http import HttpResponse
from functions import *
from teacher import models
from survey import models

@login_required
@user_passes_test(is_admin)
def index(request):
    return HttpResponse("Admin logged in!")


@login_required
@user_passes_test(is_admin)
def add_subject(request):
    if request.POST:
        subjectName = request.POST['subject']
        subject = models.Subject(subjectName=subjectName)
        subject.save()
        return HttpResponseRedirect(reverse('administrator:add_subject') + '?status=sucess')
    return render(request, 'administrator/add_subject.html')


@login_required
@user_passes_test(is_admin)
def add_teacher(request):
    if request.POST:
        username = request.POST['username']
        whichClass = request.POST['whichClass']
        subject = int(request.POST['subject'])
        teacher = models.Teacher(teacherName=username, Semester=whichClass,
                                 subject=models.Subject.objects.get(pk=subject))
        teacher.save()
        return HttpResponseRedirect(reverse('administrator:add_teacher') + '?status=success')
    allSubjects = models.Subject.objects.all()
    context = {'subjectName': allSubjects}
    return render(request, 'administrator/add_teacher.html', context=context)


def form_creation():
    for id , teacher in enumerate(models.Teacher):
        form = models.Form()
        form.formName = id
        form.teacher = models.Teacher.objects.filter(teacherName=teacher)
        form.save()
    return

@login_required
@user_passes_test(is_admin)
def survey_creation(request):
    if request.POST:
        surveyName = request.POST['surveyName']
        survey = models.Survey(surveyName = surveyName )
        survey.save()
        try:
            return HttpResponseRedirect(reverse('administrator:add_question'))
        except Exception:
            return HttpResponseRedirect(reverse('administrator:survey') + '?status=error')

    return render(request , 'administrator/survey_creation.html' )

def add_question(request):
    return