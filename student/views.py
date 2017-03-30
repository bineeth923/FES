import random
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render
from django.http import HttpResponse
from functions import *
from survey import models


def generateToken(request):
    return random.randint(100000, 999999)


def token(request, Form, tokenId):
    token = models.Token()
    token.tokenId = tokenId
    token.form = Form
    token.save()
    return


def index(request):
    tokenId = generateToken(request)
    forms = models.Form.objects.all()
    subject = []
    for form in forms:
        subject.append(form.teacher.subject.subjectName)
    context = {
        'subjectList': subject
    }
    return render(request, 'student/index.html', context)


def forms(request, formId):

    form = models.Form.objects.get(pk=int(formId))
    mcqs = models.MCQ.objects.filter(form=form)
    options = []
    for mcq in mcqs:
        options.append({'mcq': mcq, 'options': models.Options.objects.filter(mcq=mcq)})
    context = {
        'form': form,
        'options': options
    }
    return render(request, 'student/formfill.html', context)
