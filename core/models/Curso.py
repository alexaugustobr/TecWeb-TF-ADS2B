from django.db import models

class Curso(models.Model):
    #alunos = models.ManyToOneField(to='Aluno')
    sigla = models.CharField(max_length=5,unique=True,null=False)
    nome = models.CharField(max_length=50,unique=True,null=False)
    
    def __str__(self):
        return "{} - {}".format(self.sigla,self.nome)

    class Meta:
        db_table = 'Curso'


from .Matricula import Matricula
from .Aluno import Aluno