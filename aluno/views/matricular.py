from django.shortcuts import render
from django.http import HttpResponse
from core.components import *
from core.models import *
from django.http import HttpResponse
from aluno.forms.CandidatoForm import CandidatoForm


def matricular (request):
    
    codigo = request.POST.get('codigo_acesso')

    if not type(codigo) == str:
        return render(request,"matricula/formMatricula.html")

    g = GerenciadorToken()
    token = g.traduzir(codigo)

    if not g.autenticar(token):
        return render(request,"matricula/formMatricula.html")

    #buscar form do request 

    if request.POST:
        form = CandidatoForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            candidato = form.save()
            turma = Turma()
            turma.id = token.idTurma
            candidato.turma = turma
            candidato.save()
            enviarEmailConfirmacao(candidato)
    else:
        form = CandidatoForm()

    contexto = {
        "form" : form
    }

    #Salvar Candidato

    return render(request,"matricula/formMatricula.html", contexto)

def confirmarMatricula(request):

    codigo = request.GET.get('token')

    candidatoId = request.GET.get('id')

    if not type(codigo) == str:
        contexto = {
            "mensagem":"Codigo invalido"
        }
        return render(request,"matricula/confirmar.html", contexto)

    g = GerenciadorToken()
    token = g.traduzir(codigo)

    if not g.autenticar(token):
        contexto = {
            "mensagem":"Codigo invalido"
        }
        return render(request,"matricula/confirmar.html", contexto)
    
    try:
        candidato = Candidato.objects.get(id=candidatoId)
    except Exception:
        contexto = {
            "mensagem":"Candidato não encontrado"
        }
        return render(request,"matricula/confirmar.html", contexto)

    contexto = {
        "candidato":candidato,
        "mensagem":"Matricula confirmada, aguarde a aprovação do professor"
    }

    candidato.confirmado = True

    candidato.save()

    return render(request,"matricula/confirmar.html", contexto)
    

def enviarEmailConfirmacao(candidato):
    contexto = {
        "candidato":candidato
    }
    email = Email("contato@handcode.com", "Faculdade Handcode - Confirmar matricula")
    email.html("emails/contatoConfirmarMatricula.html", contexto)
    email.enviar(candidato.email)
