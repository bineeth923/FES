from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.http import HttpResponse
from functions import *
from teacher import models as teacher_view
from survey import models
from survey.views import common_login

@login_required
@user_passes_test(is_admin)
def index(request):
    return render(request, 'administrator/index.html')

@login_required
@user_passes_test(is_admin)
def logout_user(user):
    logout(user)
    return common_login(user)

@login_required
@user_passes_test(is_admin)
def add_subject(request):
    if request.POST:
        subjectName = request.POST['subject']
        subject = teacher_view.Subject(subjectName=subjectName)
        subject.save()
        return HttpResponseRedirect(reverse('administrator:add_subject') + '?status=success')
    subjects = teacher_view.Subject.objects.all()
    context = {
        'subjects': subjects,
    }
    return render(request, 'administrator/add_subject.html', context=context)


@login_required
@user_passes_test(is_admin)
def add_semester(request):
    if request.POST:
        sem = request.POST['semesterName']
        semester = teacher_view.Semester(semesterName=sem)
        semester.save()
        return HttpResponseRedirect(reverse('administrator:add_semester') + '?status=success')
    semesters = teacher_view.Semester.objects.all()
    context = {'semesters' : semesters}
    return render(request , 'administrator/add_semester.html' , context)




@login_required
@user_passes_test(is_admin)
def add_teacher(request):
    if request.POST:
        username = request.POST['username']
        semester = int(request.POST['semester'])
        subject = int(request.POST['subject'])
        teacher = teacher_view.Teacher(teacherName=username, Semester=teacher_view.Semester.objects.get(pk=semester),
                                       subject=teacher_view.Subject.objects.get(pk=subject))
        teacher.save()
        return HttpResponseRedirect(reverse('administrator:add_teacher') + '?status=success')
    allSubjects = teacher_view.Subject.objects.all()
    teachers = teacher_view.Teacher.objects.all()
    semesters = teacher_view.Semester.objects.all()
    context = {'subjectName': allSubjects,
               'teachers': teachers,
               'semesters' : semesters
               }
    return render(request, 'administrator/add_teacher.html', context=context)


def form_creation(sem):
    for id, teacher in enumerate(models.Teacher.objects.all()):
        form = models.Form()
        form.formName = id
        form.teacher = teacher
        form.semester = sem
        form.survey = models.Survey.objects.filter(sem=sem)[0]
        form.save()
    return


@login_required
@user_passes_test(is_admin)
def survey_creation(request):
    if request.POST:
        surveyName = request.POST['surveyName']
        sem = request.POST['semester']
        semester = models.Semester.objects.get(pk=int(sem))
        survey = models.Survey(surveyName=surveyName , sem = semester)
        survey.save()
        form_creation(semester)
        try:
            return HttpResponseRedirect(reverse('administrator:add_question'))
        except Exception:
            return HttpResponseRedirect(reverse('administrator:survey') + '?status=error')
    semesters = models.Semester.objects.all()
    context={
        'semesters' : semesters
    }
    return render(request, 'administrator/survey_creation.html' , context)




@login_required
@user_passes_test(is_admin)
def add_question(request):
    if request.POST:
        if request.POST['question'] == 'mcq':
            print('yeh!')
            questionText = request.POST['questionText']
            print(questionText)
            all_options = []
            for i in range(1, 6):
                all_options += [request.POST[str(i)]]
            for form in models.Form.objects.all():
                question = models.MCQ()
                question.textName = questionText
                question.form = form
                question.save()
                for option in all_options:
                    option_object = models.Options()
                    option_object.textName = option
                    option_object.result = 0
                    option_object.mcq = question
                    option_object.form = form
                    option_object.save()
            return HttpResponseRedirect(reverse('administrator:add_question') + '?status=sucess')
        elif request.POST['question'] == 'textview':
            questionText = request.POST['questionTextView']
            for form in models.Form.objects.all():
                question = models.TextView()
                question.textName = questionText
                question.result = ''
                question.form = form
                question.save()
            return HttpResponseRedirect(reverse('administrator:add_question') + '?status=success')
        else:
            return HttpResponseRedirect(reverse('administrator:add_question') + '?status=error')
    try:
        mcqs = models.MCQ.objects.filter(form=models.Form.objects.get(formName = '1'))
        if mcqs:
            textView = models.TextView.objects.filter(form = models.Form.objects.get(formName='1'))
            mcq_questions = []
            for mcq in mcqs:
                options = (models.Options.objects.filter(mcq=mcq))
                mcq_questions.append([mcq.textName, options])
            context = {'mcq_questions': mcq_questions, 'text_view_questions': textView}
        else:
            context = {}
    except:
        context = {}
    return render(request, 'administrator/add_question.html', context=context)
