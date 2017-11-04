
from django.db import models
from .Periodo import Periodo
from .Disicplina import Disicplina

class DisciplinaOfertada(models.Model):
    disciplina = models.ForeignKey(Disicplina, db_column = 'nome_disicplina')
    ano_grade = models.SmallIntegerField(null=False)
    semestre = models.CharField(max_length=1)

    class Meta:
        db_table = 'DisciplinaOfertada'