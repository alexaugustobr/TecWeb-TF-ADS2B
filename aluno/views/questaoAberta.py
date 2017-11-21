from django.shortcuts import render
from django.http import HttpResponse
from core.components import *
from core.models import *
import datetime
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'A', login_url='/login?error=acesso', redirect_field_name=None)
def questaoAberta (request, data):


    questao = None

    proxima_id = None

    anterior_id = None


    questao_id = request.GET.get('questao_id')
    anterior_questao_id = request.GET.get('anterior_questao_id')


    
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
        "anterior_id": anterior_id,
        "proxima_id": proxima_id,
        }

    return render(request,"avaliacoes/questaoAberta.html", contexto)

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'A', login_url='/login?error=acesso', redirect_field_name=None)
def questaoAbertaResponder(request):
    if request.method != 'POST':
        return HttpResponse(status=403)

    resposta = Resposta()

    resposta.descricao = request.POST.get('resposta')

    resposta.aluno = Aluno.objects.get(id=request.user.id)

    resposta.questao = Questao.objects.get(id=request.POST.get('questao_id'))

    resposta.data_de_envio = datetime.datetime.now(datetime.timezone.utc)
    
    resposta.save()


    return HttpResponse(status=200)



