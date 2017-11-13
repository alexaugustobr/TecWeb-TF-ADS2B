from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from core.models import *
from datetime import datetime
from django.core.serializers import serialize
from core.components.GerenciadorEmail import Email
from django.http import HttpResponse


def turma(request):
    assert isinstance(request, HttpRequest)

    contexto = {
        'title':'',
        'turmas': Turma.objects.all(),
    }
    return render(request,"matricula/matricula.html", contexto)


def enviarEmailTurma(request):
    if request.method != 'POST':
        return HttpResponse(status=403) 

    turma_id = request.POST.get('turma_id')

    if turma_id == None:
        return HttpResponse(status=403)
        
    turma = Turma.objects.get(id=turma_id)

    if turma == None:
        return HttpResponse(status=403)

    link = "http://localhost:8000/matricular-aluno/{}".format(turma_id)
    
    disciplina = turma.disciplinaOfertada.disciplina
    professor = turma.professor

    alunos = Aluno.objects.raw('SELECT * FROM ALUNO LEFT JOIN MATRICULA ON ALUNO.ID = MATRICULA.ALUNO_ID WHERE MATRICULA.ID IS NULL')
    
    for aluno in alunos:
        #TODO
        #gerar token
        token = "{}.{}.{}".format(aluno.id,turma.id,5654) # =)
        contexto = {
            "aluno":aluno, 
            "professor":professor, 
            "token":token, 
            "turma":turma,
            "link":link
        }
        email = Email("contato@handcode.com", "Faculdade Handcode - matricula de {} turma {}".format(disciplina.nome,turma.turma_sigla))
        email.html("emails/solicitacaoMatricula.html", contexto)
        email.enviar(aluno.email)

    contexto = {
        "alunos": alunos
    }
    
    return HttpResponse(status=200)
