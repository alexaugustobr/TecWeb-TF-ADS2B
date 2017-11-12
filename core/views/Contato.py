from django.shortcuts import render
from core.forms import ContatoForm
from core.components.GerenciadorEmail import Email

def contato (request):
    form = None

    if request.POST:
        form = ContatoForm(request.POST)
        print(form)
        if form.is_valid():
            contexto = {"aluno":form.cleaned_data['nome'], "email":form.cleaned_data['email'], "assunto":form.cleaned_data['assunto'], "mensagem":form.cleaned_data['mensagem']}
            email = Email("contato@handcode.com","Faculdade Handcode - {}".format(form.cleaned_data['assunto']))
            email.html("emails/contato.html", contexto)
            email.enviar(form.cleaned_data['email'])
    else:
        form = ContatoForm()

    contexto = {
        "form" : form
    }
    return render(request,"contato/contato.html", contexto)