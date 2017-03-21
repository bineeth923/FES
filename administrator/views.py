from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.http import HttpResponse
from functions import *


@login_required
@user_passes_test(is_admin)
def index(request):
    return HttpResponse("Admin logged in!")

