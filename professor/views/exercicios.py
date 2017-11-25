from django.shortcuts import render
from django.http import HttpResponse
from core.components import *
from core.models import *
import datetime
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'P', login_url='/login?error=acesso', redirect_field_name=None)
def exercicios (request):

    questao = None
    questao_id = request.GET.get('questao_id')
    
    sql =   "SELECT distinct questao.id, turma_id, questao.data_limite_entrega\
            FROM Questao\
            INNER JOIN Resposta\
            ON questao.id == resposta.questao_id\
            INNER JOIN Turma\
            On questao.turma_id = Turma.id\
            WHERE RESPOSTA.nota IS NULL AND Turma.professor_id ={}".format(request.user.id)
    
    questoes = Questao.objects.raw(sql)

    contexto = {"questoes" : questoes}

    return render(request,"avaliacoes/exercicios.html", contexto)

