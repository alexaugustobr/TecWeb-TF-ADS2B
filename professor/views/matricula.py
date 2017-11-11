from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from core.models.Turma import Turma
from datetime import datetime


def turma(request):
    assert isinstance(request, HttpRequest)

    contexto = {
        'title':'',
        'turmas': Turma.objects.all(),
    }
    return render(request,"matricula.html", contexto)