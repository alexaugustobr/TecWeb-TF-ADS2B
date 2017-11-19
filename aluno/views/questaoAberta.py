from django.shortcuts import render
from django.http import HttpResponse
from core.components import *
from core.models import *


def questaoAberta (request):

    questao = None

    proxima_id = None

    anterior_id = None
    #TODO buscar aluno logado
    aluno = Aluno() 
    aluno.id = 1

    i=0

    t=0

    questao_id = request.GET.get('questao_id')
    anterior_questao_id = request.GET.get('anterior_questao_id')

    
    questoes = list(Questao.objects.all())

    t=len(questoes)

    if len(questoes)>0:

        if questao_id:
            questao = Questao.objects.get(id=questao_id)
        else:
            questao = questoes[0]
        
        i=1
        for q in questoes:
            if q.id == questao.id:
                i = questoes.index(q)

        if i == len(questoes)-1:
            anterior_id = i
            proxima_id = None
        elif i < len(questoes)-1:
            proxima_id = i+2
            if i > 0:
                anterior_id = i
            else:
                anterior_id = None

    

    contexto = { 
        "questao" : questao, 
        "aluno" : aluno,
        "anterior_id": anterior_id,
        "proxima_id": proxima_id,
        "i":i,
        }

    return render(request,"avaliacoes/questaoAberta.html", contexto)

def questaoAbertaResponder(request):
    if request.method != 'POST':
        return HttpResponse(status=403)

    descricao = request.POST.get('resposta')
    aluno_id = request.POST.get('aluno_id')
    questao_id = request.POST.get('questao_id')

    resposta = Reposta()

    resposta.descricao = descricao

    reposta.save()


    return HttpResponse(status=200)



