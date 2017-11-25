from .Token import Token
from core.models import *
import datetime

class GerenciadorToken:

    def autenticar(self,token):
        aluno = Aluno.objects.filter(usuario_ptr_id=token.idAluno)

        if not aluno:
            return False

        turma = Turma.objects.filter(id=token.idTurma)

        if not turma:
            return False

        return True

    def gerar(self,aluno,turma):
        dataAtual = datetime.datetime.now(datetime.timezone.utc)
        segundos = 123
        return Token(aluno.usuario_ptr_id,turma.id,segundos)

    def traduzir(self, codigo):
        t = codigo.split('.')
        return Token(t[0],t[1],t[2])
