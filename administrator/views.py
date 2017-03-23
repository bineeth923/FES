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
    return render(request , 'administrator/index.html')


@login_required
@user_passes_test(is_admin)
def add_subject(request):
    if request.POST:
        subjectName = request.POST['subject']
        subject = teacher_view.Subject(subjectName=subjectName)
        subject.save()
        return HttpResponseRedirect(reverse('administrator:add_subject') + '?status=success')
    subjects = teacher_view.Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'administrator/add_subject.html', context=context)


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
               'teachers': teachers
               }
    return render(request, 'administrator/add_teacher.html', context=context)


def form_creation():
    for id, teacher in enumerate(models.Teacher.objects.all()):
        form = models.Form()
        form.formName = id
        form.teacher = teacher
        form.save()
    return


@login_required
@user_passes_test(is_admin)
def survey_creation(request):
    if request.POST:
        surveyName = request.POST['surveyName']
        survey = models.Survey(surveyName=surveyName)
        survey.save()
        form_creation()
        try:
            return HttpResponseRedirect(reverse('administrator:add_question'))
        except Exception:
            return HttpResponseRedirect(reverse('administrator:survey') + '?status=error')

    return render(request, 'administrator/survey_creation.html')




@login_required
@user_passes_test(is_admin)
def add_question(request):
    if request.POST:
        if request.POST['question'] == 'mcq':
            return HttpResponseRedirect(reverse('administrator:add_question_mcq'))
        elif request.POST['question'] == 'textview':
            return HttpResponseRedirect(reverse('administrator:add_question_textview'))
    mcq = models.MCQ.objects.all()
    textView = models.TextView.objects.all()
    mcq_questions = []
    options = []
    for mcq in mcq:
        for option in models.MCQ.objects.get(mcq=mcq):
            options += option
        mcq_questions += [mcq.textName, [options]]
    context = {'mcq_questions': mcq_questions, 'text_view_questions': textView}
    return render(request, 'administrator/add_question.html', context=context)
