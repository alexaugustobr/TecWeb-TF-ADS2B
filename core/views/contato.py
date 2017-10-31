from django.shortcuts import render
from core.forms import ContatoForm

def contato (request):
    
    form = None
    if request.POST:
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.envia_email()
    else:
        form = ContatoForm()
   
    contexto = {
        "form" : form
    }
    return render(request,"contato/contato.html", contexto)