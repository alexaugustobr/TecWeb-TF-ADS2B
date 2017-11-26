from django.shortcuts import render
from django.http import HttpResponse
from core.components import *
from core.models import *
import datetime
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'A', login_url='/login?error=acesso', redirect_field_name=None)
def boletim (request):
    contexto = {'respostas':Resposta.objects.raw('SELECT RESPOSTA.* FROM RESPOSTA WHERE RESPOSTA.NOTA IS NOT NULL AND RESPOSTA.ALUNO_ID = {}'.format(request.user.id))}
    return render(request,"boletim/boletim.html", contexto)