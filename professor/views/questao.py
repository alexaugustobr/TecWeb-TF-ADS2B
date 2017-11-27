from django.shortcuts import render
from professor.forms.QuestaoForm import QuestaoForm
from core.models import *
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'P', login_url='/login?error=acesso', redirect_field_name=None)
def questao (request):

        
    sql =  "SELECT turma.id, curso.sigla as 'curso', turma_sigla as 'turma', Disciplina.nome as 'disciplina' FROM Turma\
            INNER JOIN QUESTAO\
            ON Turma.id = Questao.turma_id\
            INNER JOIN Professor\
            ON Turma.professor_id = Professor.usuario_ptr_id\
            INNER JOIN DisciplinaOfertada as 'DO'\
            ON Turma.disciplinaOfertada_id = DO.id\
            INNER JOIN Disciplina\
            On DO.disciplina_id = Disciplina.id\
            Inner Join CursoTurma\
            On CursoTurma.turma_id = Turma.id\
            INNER JOIN Curso\
            On Curso.id = CursoTurma.curso_id\
            LEFT JOin Resposta\
            On Resposta.questao_id = questao.id\
            Where Resposta.aluno_id is NULL and Professor.usuario_ptr_id = {}\
            GROUP By turma".format(request.user.id)
            
    turmas = Turma.objects.raw(sql);

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