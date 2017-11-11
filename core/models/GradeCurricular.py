
from django.db import models
from .Curso import Curso

class GradeCurricular(models.Model):
    curso = models.ForeignKey(Curso, db_column='sigla_curso')
    ano = models.SmallIntegerField(null=False)
    semestre = models.CharField(max_length=1,null=False)

    class Meta:
        db_table = 'GradeCurricular'
        unique_together = ['curso', 'ano', 'semestre']