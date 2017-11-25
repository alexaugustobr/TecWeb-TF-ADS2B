from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from core.models import *
from datetime import datetime
from django.core.serializers import serialize
from core.components.GerenciadorEmail import Email
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'P', login_url='/login?error=acesso', redirect_field_name=None)
def matriculas(request):
    contexto = {
        'candidatos': Candidato.objects.all(),
    }
    return render(request,"matricula/matriculas.html", contexto)

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'P', login_url='/login?error=acesso', redirect_field_name=None)
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

def recusar(request):
    if request.method != 'POST':
        return HttpResponse(status=403) 

    turmaId = request.POST.get('turmaId')
    candidatoId = request.POST.get('candidatoId')
    candidato = Candidato.objects.get(id=candidatoId)

    turma = Turma.objects.get(id=turmaId)

    aluno = Aluno.objects.get(ra=candidato.ra)
    candidato.delete()
    return HttpResponse(status=200)
        
