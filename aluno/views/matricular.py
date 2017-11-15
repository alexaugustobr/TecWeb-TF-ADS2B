from django.shortcuts import render
from django.http import HttpResponse
from core.components import *
from core.models import *

def matricular (request):
    return render(request,"matricula/formMatricula.html")

def confirmarMatricula (request):

    codigo = request.GET.get('codigo')

    if not type(codigo) == str:
        return HttpResponse(status=400)

    g = GerenciadorToken()
    token = g.traduzir(codigo)

    if not g.autenticar(token):
        return HttpResponse(status=401)

    return HttpResponse(status=200)
