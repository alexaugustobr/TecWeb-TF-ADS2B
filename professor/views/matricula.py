from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from core.models import *
from datetime import datetime
from django.core.serializers import serialize
from core.components.GerenciadorEmail import Email
from django.http import HttpResponse


def matriculas(request):
    contexto = {
        'candidatos': Candidato.objects.all(),
    }
    return render(request,"matricula/matriculas.html", contexto)


def confirmar(request):
    if request.method != 'POST':
        return HttpResponse(status=403) 
    
    
    turmaId = request.POST.get('turmaId')
    candidatoId = request.POST.get('candidatoId')

    candidato = Candidato.objects.get(id=candidatoId)

    turma = Turma.objects.get(id=turmaId)

    aluno = Aluno.objects.get(ra=candidato.ra)

    aluno.turmas.add(turma)

    aluno.save()

    candidato.matricula_aceita = True
    
    candidato.save()
    
    return HttpResponse(status=200)