from django.shortcuts import render
from django.http import HttpResponse
from core.components import *
from core.models import *
import datetime
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'P', login_url='/login?error=acesso', redirect_field_name=None)
def exerciciosRecebidos (request, idTurma):


    questao = None

    

    questao_id = request.GET.get('questao_id')
    

    
    sql =   "SELECT turma.id, TURMA.turma_sigla\
            FROM RESPOSTA\
            INNER JOIN QUESTAO\
            ON QUESTAO.id = RESPOSTA.questao_id\
            INNER JOIN turma\
            ON QUESTAO.turma_id = turma.id\
            WHERE RESPOSTA.nota IS NULL AND TURMA.ID ={}".format(idTurma)
            
    
    respostas = list(Resposta.objects.raw(sql))

    print(respostas)

    for r in respostas:
        print(r)

    contexto = { 
        "respostas" : respostas, 
        }

    return render(request,"avaliacoes/exerciciosRecebidos.html", contexto)

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'P', login_url='/login?error=acesso', redirect_field_name=None)
def exerciciosRecebidosAvaliar(request):
    if request.method != 'POST':
        return HttpResponse(status=403)

    #request.user.id professor

    resposta = Resposta.objects.get(id=request.POST.get('resposta_id'))
    resposta.nota = request.POST.get('nota')
    resposta.data_avaliacao = datetime.datetime.now(datetime.timezone.utc)
    resposta.save()

    return HttpResponse(status=200)