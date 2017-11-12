from django.db import models

class Aluno(Usuario):
    curso = models.ForeignKey(to='Curso', related_name="alunos", null=False, blank=False) #onetomany
    email = models.CharField(max_length=80)
    celular = models.CharField(max_length=11)
    ra = models.IntegerField(unique=True,null=False)

    def __str__(self):
        return "{} - {}".format(self.ra,self.nome)
    
    class Meta:
        db_table = 'Aluno'
    

from .Matricula import Matricula
from .Curso import Curso
from .CadastroUsuarios import Usuario