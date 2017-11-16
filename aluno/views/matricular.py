from django.shortcuts import render
from django.http import HttpResponse
from core.components import *
from core.models import *

def matricular (request):
   
    codigo = request.POST.get('codigo')

    if not type(codigo) == str:
        return render(request,"matricula/formMatricula.html")

    g = GerenciadorToken()
    token = g.traduzir(codigo)

    if not g.autenticar(token):
        return render(request,"matricula/formMatricula.html")

    #buscar form do request 
    #Salvar Candidato

    return render(request,"matricula/formMatricula.html")
