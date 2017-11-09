from django.db import models

class Matricula(models.Model):
    aluno = models.ForeignKey(to='Aluno', related_name="matriculas", null=False, blank=False) #onetomany
    nome = models.CharField(max_length=120,null=False)
    email = models.CharField(max_length=80)
    celular = models.CharField(max_length=11)
    ra = models.IntegerField(unique=True,null=False)
    
    class Meta:
        db_table = 'Matricula'

from .Turma import Turma
from .Aluno import Aluno
