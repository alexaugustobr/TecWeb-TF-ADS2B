from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

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