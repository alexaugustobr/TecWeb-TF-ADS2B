from django.test import TestCase
from core.models import *

class TesteMatricula(TestCase):
    def setUp(self):
        curso = Curso()
        curso.nome = "ADS"
        curso.sigla = "ADS"
        curso.save()

        aluno = Aluno()
        aluno.curso = curso
        aluno.nome = "Alex"
        aluno.ra = 12356
        aluno.save()

        aluno = Aluno()
        aluno.curso = curso
        aluno.nome = "Dani"
        aluno.ra = 1355546
        aluno.save()




    def test_aluno_cadastrado(self):
        aluno = Aluno.objects.get(nome="Alex")
        #cat = Animal.objects.get(name="cat")
        self.assertEqual(aluno.nome, "Alex")
        #self.assertEqual(cat.speak(), 'The cat says "meow"')
        alunos = Aluno.objects.all()
        self.assertEqual(len(alunos), 2)

    def test_aluno_matriculado(self):
        alunos = Aluno.objects.raw("SELECT * FROM ALUNO LEFT JOIN MATRICULA WHERE ON ALUNO.ID = MATRICULA.ALUNO_ID WHERE MATRICULA.ID IS NULL")
        self.assertEqual(len(alunos), 2)
