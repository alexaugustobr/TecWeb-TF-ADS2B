
from django.db import models

class PeriodoDisciplina(models.Model):
    periodo = models.ForeignKey(to='Periodo', related_name="periodosDisciplina", null=False, blank=False) #onetomany
    disciplina = models.ForeignKey(to='Disciplina', related_name="periodosDisciplina", null=False, blank=False) #onetomany
    ano_grade = models.SmallIntegerField(null=False)
    semestre_grade = models.CharField(max_length=1,null=False)
    
    def __str__(self):
        return "{} - {}: {} - {}".format(self.periodo, self.disciplina, self.ano_grade, self.semestre_grade)
    class Meta:
        db_table = 'PeriodoDisciplina'

from .Periodo import Periodo
from .Disciplina import Disciplina
