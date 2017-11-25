from django.shortcuts import render
from django.http import HttpResponse
from core.components import *
from core.models import *
from django.http import HttpResponse
from aluno.forms.CandidatoForm import CandidatoForm
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'A', login_url='/login?error=acesso', redirect_field_name=None)
def matricular (request):


    codigo = None

    contexto = None

    if request.method == 'POST':
        codigo = request.POST.get('codigo_acesso')
    if request.method == 'GET':
        codigo = request.GET.get('codigo_acesso')
    

    if not type(codigo) == str:
        return render(request,"matricula/formMatricula.html")

    g = GerenciadorToken()
    token = g.traduzir(codigo)

    if not g.autenticar(token):
        return render(request,"matricula/formMatricula.html")
    
    #buscar form do request 

    if request.POST:
        form = CandidatoForm(request.POST)
        if form.is_valid():
            candidato = form.save()
            turma = Turma()
            turma.id = token.idTurma
            candidato.turma = turma
            candidato.save()
            enviarEmailConfirmacao(candidato)
            #TODO redirect
            contexto = {
                "confrimacao": "Por favor confirme a matricula por email.",
                "form" : form
            }
        else:
            contexto = {
                "form" : form
            }
    else:
        turma = Turma.objects.get(id=token.idTurma)
        aluno = Aluno.objects.get(id=token.idAluno)
        form = CandidatoForm()
        contexto = {
            "codigo_acesso":token.__str__(),
            "aluno": aluno,
            "turma": turma,
            "form" : form
        }


    #Salvar Candidato

    return render(request,"matricula/formMatricula.html", contexto)

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'A', login_url='/login?error=acesso', redirect_field_name=None)
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
