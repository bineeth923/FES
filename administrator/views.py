from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.http import HttpResponse
from functions import *
from teacher import models as teacher_view
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
        subject = teacher_view .Subject(subjectName=subjectName)
        subject.save()
        return HttpResponseRedirect(reverse('administrator:add_subject') + '?status=success')
    subjects = teacher_view.Subject.objects.all()
    context = {'subjects' : subjects}
    return render(request, 'administrator/add_subject.html' , context=context)


@login_required
@user_passes_test(is_admin)
def add_teacher(request):
    if request.POST:
        username = request.POST['username']
        whichClass = request.POST['whichClass']
        subject = int(request.POST['subject'])
        teacher = teacher_view.Teacher(teacherName=username, Semester=whichClass,
                                 subject=teacher_view.Subject.objects.get(pk=subject))
        teacher.save()
        return HttpResponseRedirect(reverse('administrator:add_teacher') + '?status=success')
    allSubjects = teacher_view.Subject.objects.all()
    teachers = teacher_view.Teacher.objects.all()
    context = {'subjectName': allSubjects,
               'teachers' : teachers
               }
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
    if request.POST:
        if request.POST['mcq']:
            HttpResponseRedirect(reverse('administrator:add_question_mcq'))
        elif request.POST['textview']:
            HttpResponseRedirect(reverse('administrator:add_question_textview'))
    mcq = models.MCQ.objects.all()
    mcq_questions = []
    for mcq in mcq:
        mcq_questions += [mcq.textName , []]
    context = {}
    return render(request , 'administrator/add_question.html' , context=context)