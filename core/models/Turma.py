
from django.db import models
from .Periodo import Periodo


class Turma(models.Model):
    disciplinaOfertada = models.ForeignKey(to='DisciplinaOfertada', related_name="turmas", null=False, blank=False) #onetomany
    professor = models.ForeignKey(to='Professor', related_name="turmas", null=False, blank=False) #onetomany
    turno = models.CharField(max_length=15)
    turma_sigla = models.CharField(max_length=1)
    cursos = models.ManyToManyField('Curso', db_table='CursoTurma', related_name='turmas', blank=False)

    def __str__(self):
        return "{} - {}".format(self.turma_sigla, self.turno)

    class Meta:
        db_table = 'Turma'

from .DisciplinaOfertada import DisciplinaOfertada
from .Professor import Professor
from .Curso import Curso