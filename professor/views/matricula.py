from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from core.models.Turma import Turma
from datetime import datetime

from django.http import HttpResponse


def turma(request):
    assert isinstance(request, HttpRequest)

    contexto = {
        'title':'',
        'turmas': Turma.objects.all(),
    }
    return render(request,"matricula.html", contexto)


def enviarEmailTurma(request):
    if request.method == 'POST':

        turma_id = request.POST.get('turma_id')
        print(turma_id)
    #/turma/enviar-email
    return HttpResponse(status=200)