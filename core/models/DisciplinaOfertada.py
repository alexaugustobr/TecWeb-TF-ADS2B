
from django.db import models
from .Periodo import Periodo
from .Disciplina import Disciplina

class DisciplinaOfertada(models.Model):
    disciplina = models.ForeignKey(Disciplina, db_column = 'nome_disicplina')
    ano_grade = models.SmallIntegerField(null=False)
    semestre = models.CharField(max_length=1)

    class Meta:
        db_table = 'DisciplinaOfertada'