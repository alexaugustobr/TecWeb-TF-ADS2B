from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from core.models import *
from datetime import datetime
from django.core.serializers import serialize
from core.components.GerenciadorEmail import Email
from django.http import HttpResponse


def matriculas(request):
    contexto = {
        'candidatos': Candidato.objects.all(),
    }
    return render(request,"matricula/matriculas.html", contexto)
