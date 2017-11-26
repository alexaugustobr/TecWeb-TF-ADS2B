from django.test import TestCase
from core.models import *
from core.components.GerenciadorToken import *
import datetime
class TesteMatricula(TestCase):
    def setUp(self):
        curso       = Curso()
        curso.nome  = "SI"
        curso.sigla = "SI"
        curso.save()

        aluno       = Aluno()
        aluno.curso = curso
        aluno.email = 'alex2@alex.com'
        aluno.nome  = "Alex"
        aluno.ra    = 12356
        aluno.save()

        aluno2        = Aluno()
        aluno2.curso  = curso
        aluno2.email = 'Dani2@Dani.com'
        aluno2.nome   = "Dani"
        aluno2.ra     = 1355546
        aluno2.save()


        curso = Curso()

        curso.sigla = "ADS"
        curso.nome  = "Analise e desenv de sistemas"

        curso.save()

        gc          = GradeCurricular()
        gc.curso    = curso
        gc.ano      = 2017
        gc.semestre = "P"
        gc.save()

        p                 = Periodo()
        p.numero          = 1
        p.ano_grade       = 2017
        p.gradeCurricular = gc
        p.save()

        d               = Disciplina()
        d.nome          = "TECWEB"
        d.carga_horaria = 10
        d.teoria        = 5
        d.pratica       = 5
        d.save()
        d.periodos.add(p)
        d.save()

        do              = DisciplinaOfertada()
        do.disciplina   = d
        do.ano          = 2017
        do.semestre     = "P"
        do.save()

        p           = Professor()
        p.nome      = "Lima"
        p.apeido    = "Lima"
        p.ra        = 123123
        p.email     = "lima@impacta.edu.br"
        p.celular   = 12345678910
        p.save()

        t                    = Turma()
        t.sigla_turma        = "A"
        t.turno              = "Manha"
        t.professor          = p
        t.disciplinaOfertada = do
        t.save()
        t.cursos.add(curso)
        t.save()

        t                    = Turma()
        t.sigla_turma        = "B"
        t.turno              = "Manha"
        t.professor          = p
        t.disciplinaOfertada = do
        t.save()
        t.cursos.add(curso)
        t.save()

        aluno2.turmas.add(t)
        aluno2.save()

    def test_aluno_cadastrado(self):
        aluno = Aluno.objects.get(nome="Alex")
        self.assertEqual(aluno.nome, "Alex")
        alunos = Aluno.objects.all()
        self.assertEqual(len(alunos), 2)

    def test_aluno_nao_matriculados(self):
        alunos = Aluno.objects.raw('SELECT * FROM ALUNO LEFT JOIN MATRICULA ON aluno.usuario_ptr_id = MATRICULA.ALUNO_ID WHERE MATRICULA.ID IS NULL')
        for aluno in alunos:
            self.assertEqual(aluno.nome, "Alex")

    def test_aluno_matriculados(self):
        alunos = Aluno.objects.raw('SELECT * FROM ALUNO INNER JOIN MATRICULA ON aluno.usuario_ptr_id = MATRICULA.ALUNO_ID')
        for aluno in alunos:
            self.assertEqual(aluno.nome, "Dani")

    def test_buscar_matriculas_do_aluno(self):
        dani = Aluno.objects.get(nome="Dani")
        matriculas_do_dani = dani.turmas.all()
        self.assertEqual(len(matriculas_do_dani), 1)

    def test_token(self):
        aluno    = Aluno()
        aluno.usuario_ptr_id = 1
        turma    = Turma()
        turma.id = 1

        g     = GerenciadorToken()
        token = g.gerar(aluno,turma)

        segundos = token.segundos

        self.assertEqual(g.autenticar(token),True)
        
    def test_token_2(self):
        aluno    = Aluno()
        aluno.usuario_ptr_id = 0
        turma    = Turma()
        turma.id = 0
        
        g     = GerenciadorToken()
        token = g.gerar(aluno,turma)

        segundos = token.segundos

        self.assertEqual(g.autenticar(token),False)
        
    def test_token_3(self):
        
        g     = GerenciadorToken()
        token = g.traduzir("1.1.324343")

        self.assertEqual(g.autenticar(token),True)

    def test_token_4(self):
        
        g     = GerenciadorToken()
        token = g.traduzir("0.0.324343")

        self.assertEqual(g.autenticar(token),False)



    def test_matricula_mesma_disciplina(self):
        alunos = Aluno.objects.raw('SELECT ALUNO.* FROM ALUNO \
                                LEFT JOIN MATRICULA \
                                ON aluno.usuario_ptr_id = MATRICULA.ALUNO_ID \
                                LEFT JOIN TURMA \
                                ON turma.id = MATRICULA.turma_id \
                                LEFT JOIN DisciplinaOfertada \
                                ON DisciplinaOfertada.id = TURMA.disciplinaOfertada_id \
                                WHERE disciplinaOfertada_id NOT IN (SELECT disciplinaOfertada_id FROM TURMA WHERE TURMA.ID = {}) OR disciplinaOfertada_id IS NULL'.format(1))
        for aluno in alunos:
            self.assertEqual(aluno.nome,'Alex')