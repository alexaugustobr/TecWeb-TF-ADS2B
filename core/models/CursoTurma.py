from django.db import models

class CursoTurma(models.Model):
    turma = models.ForeignKey(to='Turma', related_name="cursoTurmas", null=False, blank=False) #onetomany
    curso = models.ForeignKey(to='Curso', related_name="cursoTurmas", null=False, blank=False) #onetomany
    
    def __str__(self):
        return "{} - {}".format(self.curso.sigla,self.turma.turma_sigla)

    class Meta:
        db_table = 'CursoTurma'

from .Turma import Turma
from .Curso import Curso
