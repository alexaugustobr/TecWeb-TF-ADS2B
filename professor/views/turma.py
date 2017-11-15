from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from core.models import *
from datetime import datetime
from django.core.serializers import serialize
from core.components.GerenciadorEmail import Email
from django.http import HttpResponse


def turmaDetalhe(request, idTurma):
    #TODO buscar turma do professor
    contexto = {
        'title':'',
        'alunos': Aluno.objects.all(),
        'candidatos': Candidato.objects.all(),
    }
    return render(request,"turma/turma.html", contexto)

def turmas(request):
    #TODO buscar turma do professor
    contexto = {
        'title':'',
        'turmas': Turma.objects.all(),
    }
    return render(request,"turma/turmas.html", contexto)
