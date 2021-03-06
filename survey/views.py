import sys
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from functions import is_student, is_admin, is_teacher
from student.views import generateToken
from survey import models

class UserGroupException(Exception):
    pass


def redirect_index(user):
    try:
        if is_admin(user):
            return HttpResponseRedirect(reverse('administrator:index'))
        elif is_teacher(user):
            return HttpResponseRedirect(reverse('teacher:index'))
    except:
        raise UserGroupException


def common_login(request):
    if request.POST:
        if request.POST['userType']=='admin':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect_index(user)
            else:
                return HttpResponseRedirect(reverse('login') + '?status=auth-error')
        elif request.POST['userType']=='student':
            request.session['token'] = generateToken(request)
            token = models.Token()
            token.tokenId = str(request.session.get('token'))
            print(str(request.session.get('token')))
            token.save()
            return HttpResponseRedirect(reverse('student:index') + '?token=' + str(request.session.get('token')))
    return render(request, 'survey/index.html' )


