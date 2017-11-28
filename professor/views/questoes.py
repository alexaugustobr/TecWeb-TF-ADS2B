from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from core.models import *

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'P', login_url='/login?error=acesso', redirect_field_name=None)
def questoes (request):
    
    questao = None
    questao_id = request.GET.get('questao_id')
    
    sql =   "SELECT * FROM Questao\
            INNER JOIN Turma\
            On questao.turma_id = Turma.id\
            WHERE Turma.professor_id ={}".format(request.user.id)
    
    questoes = Questao.objects.raw(sql)

    contexto = {"questoes" : questoes}
    
    return render (request,"avaliacoes/questoes.html", contexto)

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'P', login_url='/login?error=acesso', redirect_field_name=None)
def excluirExercicio(request):
    if request.method != 'POST':
        return HttpResponse(status=403) 
    
    questaoId = request.POST.get('questaoId')
    questao = Questao.objects.get(id=questaoId)
    questao.delete()
    return JsonResponse({'mensagem': 'Exercício removido.'})