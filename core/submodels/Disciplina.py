
from django.db import models
from .Periodo import Periodo

class Disciplina(models.Model):
    nome = models.CharField(max_length=240,primary_key=True,null=False)
    carga_horaria = models.SmallIntegerField()  #tinyint
    teoria = models.DecimalField(max_digits=3,decimal_places=2)
    pratica = models.DecimalField(max_digits=3,decimal_places=2)
    ementa = models.TextField()
    competencias = models.TextField()
    habilidades = models.TextField()
    conteudo = models.TextField()
    bibliografia_complementar = models.TextField()
    bibliografia_basica = models.TextField()

    class Meta:
        db_table = 'Disciplina'