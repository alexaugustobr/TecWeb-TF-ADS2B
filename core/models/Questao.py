
from django.db import models
from .Periodo import Periodo
from .DisciplinaOfertada import DisciplinaOfertada
from .Turma import Turma

class Questao(models.Model):
    descricao = models.TextField()
    data_limite_entrega = models.DateField()
    numero = models.IntegerField()
    data = models.DateField()
    class Meta:
        db_table = 'Questao'