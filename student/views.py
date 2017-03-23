from django.contrib.auth.decorators import  user_passes_test, login_required
from django.shortcuts import render
from django.http import HttpResponse
from functions import *


@login_required
@user_passes_test(is_student)
def index(request):
    return HttpResponse("Student logged in!")

