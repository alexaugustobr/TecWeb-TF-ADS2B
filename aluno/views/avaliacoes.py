from django.shortcuts import render
from django.http import HttpResponse
from core.components import *
from core.models import *
import datetime
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'A', login_url='/login?error=acesso', redirect_field_name=None)
def avaliacoes (request):


    sql =   "SELECT QUESTAO.* FROM QUESTAO\
            INNER JOIN TURMA\
            ON TURMA.ID = QUESTAO.TURMA_ID\
            INNER JOIN CURSOTURMA\
            ON TURMA.ID = CURSOTURMA.turma_id\
            INNER JOIN MATRICULA\
            ON MATRICULA.turma_id = TURMA.id\
            LEFT JOIN RESPOSTA \
            ON RESPOSTA.questao_id = QUESTAO.ID\
            WHERE RESPOSTA.aluno_id != {0} AND MATRICULA.aluno_id = {0} AND DATA_LIMITE_ENTREGA >= '{1}' GROUP BY DATA".format(request.user.id,str(datetime.date.today()))

    questoes = list(Questao.objects.raw(sql))

    contexto = { 
        "questoes" : questoes,
        }

    return render(request,"avaliacoes/avaliacoes.html", contexto)