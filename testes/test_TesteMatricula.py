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
        aluno.nome  = "Alex"
        aluno.ra    = 12356
        aluno.save()

        aluno2        = Aluno()
        aluno2.curso  = curso
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

        aluno2.turmas.add(t)
        aluno2.save()

    def test_aluno_cadastrado(self):
        aluno = Aluno.objects.get(nome="Alex")
        #cat = Animal.objects.get(name="cat")
        self.assertEqual(aluno.nome, "Alex")
        #self.assertEqual(cat.speak(), 'The cat says "meow"')
        alunos = Aluno.objects.all()
        self.assertEqual(len(alunos), 2)

    def test_aluno_nao_matriculados(self):
        alunos = Aluno.objects.raw('SELECT * FROM ALUNO LEFT JOIN MATRICULA ON ALUNO.ID = MATRICULA.ALUNO_ID WHERE MATRICULA.ID IS NULL')
        for aluno in alunos:
            self.assertEqual(aluno.nome, "Alex")

    def test_aluno_matriculados(self):
        alunos = Aluno.objects.raw('SELECT * FROM ALUNO INNER JOIN MATRICULA ON ALUNO.ID = MATRICULA.ALUNO_ID')
        for aluno in alunos:
            self.assertEqual(aluno.nome, "Dani")

    def test_buscar_matriculas_do_aluno(self):
        dani = Aluno.objects.get(nome="Dani")
        matriculas_do_dani = dani.turmas.all()
        self.assertEqual(len(matriculas_do_dani), 1)

    def test_token(self):
        aluno    = Aluno()
        aluno.id = 1
        turma    = Turma()
        turma.id = 1

        g     = GerenciadorToken()
        token = g.gerar(aluno,turma)

        segundos = token.segundos

        self.assertEqual(g.autenticar(token),True)
        #self.assertEqual(token.__str__(),"{}.{}.{}".format(1,1,segundos))

    def test_token_2(self):
        aluno    = Aluno()
        aluno.id = 0
        turma    = Turma()
        turma.id = 0
        
        g     = GerenciadorToken()
        token = g.gerar(aluno,turma)

        segundos = token.segundos

        self.assertEqual(g.autenticar(token),False)
        #self.assertEqual(token.__str__(),"{}.{}.{}".format(1,1,segundos))
    def test_token_3(self):
        
        g     = GerenciadorToken()
        token = g.traduzir("1.1.324343")

        self.assertEqual(g.autenticar(token),True)

    def test_token_4(self):
        
        g     = GerenciadorToken()
        token = g.traduzir("0.0.324343")

        self.assertEqual(g.autenticar(token),False)