from .Token import Token
from core.models import *
import datetime

class GerenciadorToken:

    def autenticar(self,token):
        aluno = Aluno.objects.get(id=token.idAluno)

        if not aluno:
            return False

        turma = Aluno.objects.get(id=token.idTurma)

        if not turma:
            return False

        return True

    def gerar(self,aluno,turma):
        dataAtual = datetime.datetime.now(datetime.timezone.utc)
        segundos = dataAtual.strftime('%s')
        return Token(aluno.id,turma.id,segundos)