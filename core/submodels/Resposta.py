
from django.db import models
from .Curso import Curso

class Reposta(models.Model):
    aluno = models.ForeignKey(to='Aluno', related_name="matriculas", null=False, blank=False) #onetomany
    data_avaliacao = models.DateField()
    nota = models.DecimalField(max_digits=4,decimal_places=2)
    avaliacao = models.TextField()
    descricao = models.TextField()
    data_de_envio = models.TextField()

    class Meta:
        db_table = 'Reposta'