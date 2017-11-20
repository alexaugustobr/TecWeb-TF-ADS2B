from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from core.models import *
from datetime import datetime
from django.core.serializers import serialize
from core.components.GerenciadorEmail import Email
from django.http import HttpResponse

from core.components.GerenciadorToken import GerenciadorToken
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'P', login_url='/login?error=acesso', redirect_field_name=None)
def turma(request, idTurma):
    #TODO buscar turma do professor

    #turma = Turma.objects.get(id=idTurma)

    contexto = {
        'alunos': Aluno.objects.raw('SELECT * FROM ALUNO INNER JOIN MATRICULA ON aluno.usuario_ptr_id = MATRICULA.ALUNO_ID WHERE MATRICULA.TURMA_ID IS '+idTurma),
    }
    return render(request,"turma/turma.html", contexto)

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'P', login_url='/login?error=acesso', redirect_field_name=None)
def turmas(request):
    #TODO buscar turma do professor
    contexto = {
        'turmas': Turma.objects.all(),
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

    alunos = Aluno.objects.raw('SELECT * FROM ALUNO LEFT JOIN MATRICULA ON aluno.usuario_ptr_id = MATRICULA.ALUNO_ID WHERE MATRICULA.ID IS NULL')
    
    for aluno in alunos:
        #TODO
        #gerar token
        gt = GerenciadorToken()
         
        token = gt.gerar(aluno,turma)
        s = token.__str__()
        contexto = {
            "aluno":aluno, 
            "professor":professor, 
            "codigo_acesso":token.__str__(),
            "turma":turma
        }
        email = Email("contato@handcode.com", "Faculdade Handcode - matricula de {} turma {}".format(disciplina.nome,turma.turma_sigla))
        email.html("emails/solicitacaoMatricula.html", contexto)
        email.enviar(aluno.email)

    contexto = {
        "alunos": alunos
    }
    
    return HttpResponse(status=200)
