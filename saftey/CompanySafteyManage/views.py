
# -*- coding: utf-8 -*-
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import request
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login/')
def index(request):
    username = request.user.username
    return render(request, r'index.html', {'username': username})


def add_project(request):
    return render(request, r'project\add.html')


def list_project(request):
    return render(request, r'project\list.html')


def delete_project(request, id):
    return HttpResponse(request, json.dumps({'status': 'OK'}))


def edite_project(request, id):
    return render(request, r'project\edite.html')
