from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from core.components import *
from core.models import *
import datetime
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'P', login_url='/login?error=acesso', redirect_field_name=None)
def exerciciosPendentes (request, idTurma):

    turma = None
    try:
        turma = Turma.objects.get(id=idTurma)
    except expression as identifier:
        return HttpResponseRedirect("/professor")
   

    if turma:
        if turma.professor.usuario_ptr_id != request.user.id:
             return HttpResponseRedirect("/professor")
    
    turmas = None         
    usuario = None
    turmas_id = request.GET.get('turmas_id')
    usuario_id = request.GET.get('usuario_id')
    

    
    sql =  "SELECT usuario.id, usuario.nome, data_limite_entrega as data_limite,\
            curso.sigla as 'curso', turma_sigla as 'turma', disciplina.nome\
            as 'disciplina', questao.numero as 'exercicio' FROM usuario\
            INNER JOIN ALUNO \
            ON Aluno.usuario_ptr_id = usuario.id\
            INNER JOIN Matricula\
            On Aluno.usuario_ptr_id = Matricula.aluno_id\
            INNER JOIN TURMA\
            ON Matricula.turma_id = Turma.id\
            INNER JOIN QUESTAO\
            ON Turma.id = Questao.turma_id\
            INNER JOIN Professor\
            ON Turma.professor_id = Professor.usuario_ptr_id\
            INNER JOIN DisciplinaOfertada as 'DO'\
            ON Turma.disciplinaOfertada_id = DO.id\
            INNER JOIN Disciplina\
            On DO.disciplina_id = Disciplina.id\
            Inner Join CursoTurma\
            On CursoTurma.turma_id = Turma.id\
            INNER JOIN Curso\
            On Curso.id = CursoTurma.curso_id\
            LEFT JOin Resposta\
            On Resposta.questao_id = questao.id\
            Where Resposta.aluno_id is NULL and Matricula.turma_id ={} and Professor.usuario_ptr_id = {}\
            ORDER BY usuario.nome".format(idTurma, request.user.id)


    sql2 =  "SELECT usuario.id, curso.sigla as 'curso', turma_sigla as 'turma', turma.id as turma_id, Disciplina.nome as 'disciplina' FROM usuario \
            INNER JOIN ALUNO \
            ON Aluno.usuario_ptr_id = usuario.id\
            INNER JOIN Matricula\
            On Aluno.usuario_ptr_id = Matricula.aluno_id\
            INNER JOIN TURMA\
            ON Matricula.turma_id = Turma.id\
            INNER JOIN QUESTAO\
            ON Turma.id = Questao.turma_id\
            INNER JOIN Professor\
            ON Turma.professor_id = Professor.usuario_ptr_id\
            INNER JOIN DisciplinaOfertada as 'DO'\
            ON Turma.disciplinaOfertada_id = DO.id\
            INNER JOIN Disciplina\
            On DO.disciplina_id = Disciplina.id\
            Inner Join CursoTurma\
            On CursoTurma.turma_id = Turma.id\
            INNER JOIN Curso\
            On Curso.id = CursoTurma.curso_id\
            LEFT JOin Resposta\
            On Resposta.questao_id = questao.id\
            Where Resposta.aluno_id is NULL and Professor.usuario_ptr_id = {}\
            GROUP By turma".format(request.user.id)
            
    turmas = Usuario.objects.raw(sql2)
    usuarios = Usuario.objects.raw(sql)

    contexto = { 
        "usuarios" : usuarios,
        "turmas" : turmas, 
        }

    return render(request,"avaliacoes/exerciciosPendentes.html", contexto)
