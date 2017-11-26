from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from core.models import *
from datetime import datetime
from django.core.serializers import serialize
from django.core import serializers
from core.components.GerenciadorEmail import Email
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse

import json
from core.components.GerenciadorToken import GerenciadorToken
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'P', login_url='/login?error=acesso', redirect_field_name=None)
def turma(request, idTurma):
    #TODO buscar turma do professor
    turma = None
    try:
        turma = Turma.objects.get(id=idTurma)
    except expression as identifier:
        return HttpResponseRedirect("/professor/turmas")
   

    if turma:
        if turma.professor.usuario_ptr_id != request.user.id:
             return HttpResponseRedirect("/professor/turmas")
    else:
        return HttpResponseRedirect("/professor/turmas")

    contexto = {
        'alunos': Aluno.objects.raw('SELECT * FROM ALUNO INNER JOIN MATRICULA ON aluno.usuario_ptr_id = MATRICULA.ALUNO_ID WHERE MATRICULA.TURMA_ID IS '+idTurma),
    }
    return render(request,"turma/turma.html", contexto)

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'P', login_url='/login?error=acesso', redirect_field_name=None)
def turmas(request):
    #TODO buscar turma do professor
    sql =   "SELECT * FROM Turma\
            WHERE Turma.professor_id ={}".format(request.user.id)
    
    turmas = Turma.objects.raw(sql)
    
    contexto = {
        'turmas': turmas,
    }

    return render(request,"turma/turmas.html", contexto)

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'P', login_url='/login?error=acesso', redirect_field_name=None)
def enviarEmailTurma(request):
    if request.method != 'POST':
        return HttpResponse(status=403) 

    turma_id = request.POST.get('turma_id')

    if turma_id == None:
        return HttpResponse(status=403)
        
    turma = Turma.objects.get(id=turma_id)

    if turma == None:
        return HttpResponse(status=403)

    disciplina = turma.disciplinaOfertada.disciplina
    professor = turma.professor

    alunos = Aluno.objects.raw('SELECT ALUNO.* FROM ALUNO \
                                LEFT JOIN MATRICULA \
                                ON aluno.usuario_ptr_id = MATRICULA.ALUNO_ID \
                                LEFT JOIN TURMA \
                                ON turma.id = MATRICULA.turma_id \
                                LEFT JOIN DisciplinaOfertada \
                                ON DisciplinaOfertada.id = TURMA.disciplinaOfertada_id \
                                WHERE disciplinaOfertada_id NOT IN (SELECT disciplinaOfertada_id FROM TURMA WHERE TURMA.ID = {}) OR disciplinaOfertada_id IS NULL').format(turma_id)
                                    
    for aluno in alunos:
        print(aluno.usuario_ptr_id)
        gt = GerenciadorToken()
         
        token = gt.gerar(aluno,turma)
        s = token.__str__()
        contexto = {
            "aluno":aluno, 
            "professor":professor, 
            "codigo_acesso":token.__str__(),
            "turma":turma
        }
        print(token.__str__())
        email = Email("contato@handcode.com", "Faculdade Handcode - matricula de {} turma {}".format(disciplina.nome,turma.turma_sigla))
        email.html("emails/solicitacaoMatricula.html", contexto)
        email.enviar(aluno.email)

    contexto = {
        "alunos": alunos
    }
    
    return HttpResponse(status=200)



@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'P', login_url='/login?error=acesso', redirect_field_name=None)
def APIturmas(request):

    curso_id = request.GET.get('cursoId')

    print(curso_id)

    professor_id = request.user.id

    turmas = list(Turma.objects.filter().values())



    return JsonResponse({'turmas': turmas})