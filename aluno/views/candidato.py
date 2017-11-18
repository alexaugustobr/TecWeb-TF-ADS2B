from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from core.models.Turma import Turma
from datetime import datetime
from aluno.forms.CandidatoForm import *
from django.http import HttpResponse


def candidatoForm(request):
    form = None
    print('candidato')
    if request.POST:
        print('candidato post')
        form = CandidatoForm(request.POST)
        if form.is_valid():
            form.save()
            print('salvo')
    else:
        form = CandidatoForm()

    contexto = {
        "form" : form
    }
    return render(request,"matricula/candidatoForm.html",contexto)