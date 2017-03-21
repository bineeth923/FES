import sys
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from functions import is_student, is_admin, is_teacher


class UserGroupException(Exception):
    pass


def redirect_index(user):
    try:
        if is_student(user):
            return HttpResponseRedirect(reverse('student:index'))
        elif is_admin(user):
            return HttpResponseRedirect(reverse('administrator:index'))
        elif is_teacher(user):
            return HttpResponseRedirect(reverse('teacher:index'))
    except:
        raise UserGroupException


def common_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        print(username + password)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect_index(user)
        else:
            return HttpResponseRedirect(reverse('login') + '?status=auth-error')
    return render(request, 'survey/index.html', )


