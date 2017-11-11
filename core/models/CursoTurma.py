from django.db import models

class CursoTurma(models.Model):
    turma = models.ForeignKey(to='Turma', related_name="cursoTurmas", null=False, blank=False) #onetomany
    curso = models.ForeignKey(to='Curso', related_name="cursoTurmas", null=False, blank=False) #onetomany
    
    class Meta:
        db_table = 'CursoTurma'

from .Turma import Turma
from .Curso import Curso
