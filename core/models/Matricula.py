from django.db import models

class Matricula(models.Model):
    turma = models.ForeignKey(to='Turma', related_name="matriculas", null=False, blank=False) #onetomany
    aluno = models.ForeignKey(to='Aluno', related_name="matriculas", null=False, blank=False) #onetomany
    
    def __str__(self):
        return "{}: {}".format(self.turma, self.aluno)

    class Meta:
        db_table = 'Matricula'

from .Turma import Turma
from .Aluno import Aluno
