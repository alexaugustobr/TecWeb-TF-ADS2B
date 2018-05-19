
from django.db import models
from .GradeCurricular import GradeCurricular

class Periodo(models.Model):
    gradeCurricular = models.ForeignKey(on_delete=models.CASCADE, to='GradeCurricular', related_name="periodos", null=False, blank=False) #onetomany
    numero = models.SmallIntegerField(null=False) #tinyint
    disciplinas = models.ManyToManyField('Disciplina', db_table='PeriodoDisicplina', related_name='periodos', blank=False)

    def __str__(self):
        return "{}: {} - {}".format(self.numero)

    class Meta:
        db_table = 'Periodo'
       
from .Disciplina import Disciplina