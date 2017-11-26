from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from core.models import *
from datetime import datetime
from django.core.serializers import serialize
from django.http import JsonResponse

import json
from core.components.GerenciadorEmail import Email
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'P', login_url='/login?error=acesso', redirect_field_name=None)
def matriculas(request):

    sql =   "SELECT Candidado.* FROM Candidado\
            INNER JOIN TURMA\
            ON Candidado.turma_id = Turma.id\
            WHERE Turma.professor_id = {} ".format(request.user.id)
    
    candidatos = Candidato.objects.raw(sql);

    contexto = {
        'candidatos': candidatos,
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
    
    candidato.delete()
    
    alunos = list(Aluno.objects.raw('SELECT ALUNO.* FROM ALUNO \
                                    INNER JOIN TURMA \
                                    ON TURMA.ID = MATRICULA.turma_id\
                                    INNER JOIN MATRICULA \
                                    ON MATRICULA.aluno_id = ALUNO.usuario_ptr_id\
                                    WHERE TURMA.ID = {}'.format(turmaId)))
    q = 0
    mensagem = ''
    if alunos:
        q = len(alunos)
        if len(alunos) > 30:
            mensagem = "Aluno matricula na turma, total de alunos {}, atenção esta turma esta com a capacidade de alunos acima da capacidade recomendável de 30 alunos.".format(q)
        else:
            mensagem = "Aluno matricula na turma, total de alunos {}".format(q)
            
    return JsonResponse({'mensagem': mensagem})

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'P', login_url='/login?error=acesso', redirect_field_name=None)
def recusar(request):
    if request.method != 'POST':
        return HttpResponse(status=403) 
    
    candidatoId = request.POST.get('candidatoId')
    candidato = Candidato.objects.get(id=candidatoId)
    candidato.delete()
    return JsonResponse({'mensagem': 'Candidatura removida.'})
        
