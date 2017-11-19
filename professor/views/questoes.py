from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

from core.models import *

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'P', login_url='/login?error=acesso', redirect_field_name=None)
def questoes (request):
    
    contexto = {
        'questoes': Questao.objects.all
    }
    
    return render (request,"avaliacoes/questoes.html", contexto)