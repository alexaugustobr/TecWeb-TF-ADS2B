from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from core.models.Turma import Turma
from datetime import datetime

from django.http import HttpResponse


def confirmaToken(request):
    return render(request,"matricula/confirmaToken.html")

def formMatricula(request):
    return render(request,"matricula/formMatricula.html")