
from django.db import models
from .GradeCurricular import GradeCurricular

class Periodo(models.Model):
    gradeCurricular = models.ForeignKey(GradeCurricular, db_column='sigla_curso')
    ano_grade = models.SmallIntegerField(null=False)
    semestre_grade = models.CharField(max_length=1,null=False)
    numero = models.SmallIntegerField(null=False) #tinyint

    class Meta:
        db_table = 'Periodo'
       