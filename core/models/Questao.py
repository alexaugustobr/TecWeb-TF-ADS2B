
from django.db import models
from .Periodo import Periodo
from .DisciplinaOfertada import DisciplinaOfertada
from .Turma import Turma

class Questao(models.Model):
    turma = models.ForeignKey(to='Turma', related_name="questoes", null=False, blank=False) #onetomany
    descricao = models.TextField()
    data_limite_entrega = models.DateField()
    numero = models.IntegerField()
    data = models.DateField()

    def __str__(self):
        return "{} - {}: {}".format(self.turma.turma_sigla, self.id, self.descricao)

    class Meta:
        db_table = 'Questao'