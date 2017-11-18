from django.shortcuts import render
from professor.forms.QuestaoForm import QuestaoForm
from core.models import *


def questao (request):
    turmas = Turma.objects.all()

    form = None
    if request.POST:

        form = QuestaoForm(request.POST)


        if form.is_valid():

            turma_id = form.cleaned_data['turma_id']
            turma = Turma.objects.get(id=turma_id)
            q = Questao()
            q.turma = turma
            q.descricao = form.cleaned_data['descricao']
            q.data_limite_entrega = form.cleaned_data['data_limite']
            q.numero = form.cleaned_data['numero']
            q.data = form.cleaned_data['data']
            q.save()

    else:
        form = QuestaoForm()

    contexto = {
        "turmas":turmas,
        "form" : form
    }

    return render(request,"avaliacoes/questao.html",contexto)