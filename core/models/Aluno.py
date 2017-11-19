from django.db import models
from .Usuario import Usuario
class Aluno(Usuario):
    curso = models.ForeignKey(to='Curso', related_name="alunos", null=False, blank=False) #onetomany
    #nome = models.CharField(max_length=120,null=False)
    #email = models.CharField(max_length=80)
    celular = models.CharField(max_length=11, null=True, blank=True)
    #ra = models.IntegerField(unique=True,null=False)
    turmas = models.ManyToManyField('Turma', db_table='Matricula', related_name='alunos', blank=True)
    foto = models.ForeignKey(to='ArquivosFoto', related_name="alunos", null=True, blank=True) #onetomany

    def __str__(self):
        return "{} - {}".format(self.ra,self.nome)
    
    class Meta:
        db_table = 'Aluno'
    

from .Curso import Curso
from .Turma import Turma
from .ArquivosFoto import ArquivosFoto
