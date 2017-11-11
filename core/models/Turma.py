
from django.db import models
from .Periodo import Periodo


class Turma(models.Model):
    disciplinaOfertada = models.ForeignKey(to='DisciplinaOfertada', related_name="turmas", null=False, blank=False) #onetomany
    professor = models.ForeignKey(to='Professor', related_name="turmas", null=False, blank=False) #onetomany
    turno = models.CharField(max_length=15)
    turma_sigla = models.CharField(max_length=1)

    class Meta:
        db_table = 'Turma'

from .DisciplinaOfertada import DisciplinaOfertada
from .Professor import Professor