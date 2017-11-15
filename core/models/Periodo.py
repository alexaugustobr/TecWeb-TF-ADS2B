
from django.db import models
from .GradeCurricular import GradeCurricular

class Periodo(models.Model):
    gradeCurricular = models.ForeignKey(to='GradeCurricular', related_name="periodos", null=False, blank=False) #onetomany
    numero = models.SmallIntegerField(null=False) #tinyint
    disciplinas = models.ManyToManyField('Disciplina', db_table='PeriodoDisicplina', related_name='periodos', blank=False)

    def __str__(self):
        return "{}: {} - {}".format(self.gradeCurricular, self.ano_grade, self.semestre_grade)

    class Meta:
        db_table = 'Periodo'
       
from .Disciplina import Disciplina