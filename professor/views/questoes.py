from django.shortcuts import render

from core.models import *


def questoes (request):
    
    contexto = {
        'questoes': Questao.objects.all
    }
    
    return render (request,"avaliacoes/questoes.html", contexto)