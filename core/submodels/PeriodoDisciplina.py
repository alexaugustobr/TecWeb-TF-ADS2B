
from django.db import models
from .Periodo import Periodo
from .Disciplina import Disciplina

class PeriodoDisciplina(models.Model):
    periodo = models.ForeignKey(Periodo, db_column='numero_periodo')
    ano_grade = models.SmallIntegerField(null=False)
    semestre_grade = models.CharField(max_length=1,null=False)
    disciplina = models.ForeignKey(Disciplina, db_column = 'nome_disicplina')

    class Meta:
        db_table = 'PeriodoDisciplina'
        unique_together = ['periodo', 'ano_grade', 'semestre_grade', 'periodo', 'disciplina']