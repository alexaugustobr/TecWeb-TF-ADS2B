
from django.db import models
from .Periodo import Periodo
from .DisciplinaOfertada import DisciplinaOfertada
from .Professor import Professor

class Turma(models.Model):
    #nome_disicplina =models.CharField(max_length=240)
    #disciplina = models.ForeignObject(Professor, from_fields=['nome_disciplina'], to_fields=['nome'],  on_delete = models.CASCADE)
    ano_grade = models.SmallIntegerField(null=False)
    turno = models.CharField(max_length=15)
    #ra_professor = models.IntegerField()
    #professor = models.ForeignObject(Professor, from_fields=['ra_professor'], to_fields=['ra'],  on_delete = models.CASCADE)
    class Meta:
        db_table = 'Turma'