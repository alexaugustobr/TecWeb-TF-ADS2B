
from django.db import models
from .Periodo import Periodo
from .Disicplina import Disicplina

class Turma(models.Model):
    disciplina = models.ForeignKey(Disicplina, db_column = 'nome_disicplina')
    ano_grade = models.SmallIntegerField(null=False)

    class Meta:
        db_table = 'Turma'