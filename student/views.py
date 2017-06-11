import random
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render
from django.http import HttpResponse
from functions import *
from survey import models
from teacher import models as teacher_view


def generateToken(request):
    return random.randint(100000, 999999)


def index(request):
    if request.POST:
        form = models.Form.objects.get(formName=request.POST['form'])
        mcqs = models.MCQ.objects.filter(form=form).filter(token__isnull=True)
        textViews = models.TextView.objects.filter(form=form).filter(token__isnull=True)
        token = models.Token.objects.get(tokenId=request.session.get('token'))
        for id, mcq in enumerate(mcqs):
            # token.mcq = mcq
            MCQ = models.MCQ()
            MCQ.token = models.Token.objects.get(tokenId=request.session.get('token'))
            MCQ.textName = mcq.textName
            MCQ.form = mcq.form
            # mcq.token = models.Token.objects.get(tokenId=request.session.get('token'))
            mcq_options = models.Options.objects.filter(mcq=mcq)
            # options.token = models.Token.objects.get(tokenId=request.session.get('token'))
            #print(request.POST[str(id)])
            o = mcq_options[int(request.POST[str(id)])]
            o.result += 1
            o.save()
            print(str(id) + ':' + str(o.result))
            MCQ.save()
        for id, textView in enumerate(textViews):
            # token.textview = textView
            TextView = models.TextView()
            TextView.textName = textView.textName
            TextView.form = textView.form
            TextView.token = models.Token.objects.get(tokenId=request.session.get('token'))
            # textView.token = models.Token.objects.get(tokenId=request.session.get('token'))
            TextView.result = request.POST[textView.textName]
            TextView.save()
        token.form = form
        token.survey = form.survey
        token.save()
        # form.token = models.Token.objects.get(tokenId=request.session.get('token'))
        # form.save(force_update=True)
    semesters = teacher_view.Semester.objects.all()
    primaryKey = []
    for semester in semesters:
        primaryKey.append(semester.pk)
    zipped_data = zip(semesters, primaryKey)
    context = {
        'zippedData': zipped_data,
        'token' : request.session.get('token')
    }
    return render(request, 'student/index.html', context)


def allFroms(request, sem):
    forms = models.Form.objects.filter(semester=models.Semester.objects.get(pk=int(sem))).filter()
    primaryKey = []
    for form in forms:
        primaryKey.append(form.pk)
    zipped_data = zip(forms, primaryKey)
    context = {
        'zippedData': zipped_data,
        'token' : request.session.get('token')
    }
    return render(request, 'student/form.html', context)


def formFill(request, formId):
    form = models.Form.objects.get(pk=int(formId))
    mcqs = models.MCQ.objects.filter(form=form).filter(token__isnull=True)
    textView = models.TextView.objects.filter(form=form).filter(token__isnull=True)
    options = []
    for mcq in mcqs:
        options.append({'mcq': mcq, 'options': models.Options.objects.filter(mcq=mcq)})

    context = {
        'form': form,
        'options': options,
        'textView': textView,
        'token' : request.session.get('token')
    }
    return render(request, 'student/formfill.html', context)
