
from django.db import models
from .Periodo import Periodo

class Disciplina(models.Model):
    nome = models.CharField(max_length=240)
    carga_horaria = models.SmallIntegerField()  #tinyint
    teoria = models.DecimalField(max_digits=3,decimal_places=2)
    pratica = models.DecimalField(max_digits=3,decimal_places=2)
    ementa = models.TextField()
    competencias = models.TextField()
    habilidades = models.TextField()
    conteudo = models.TextField()
    bibliografia_complementar = models.TextField()
    bibliografia_basica = models.TextField()

    def __str__(self):
        return "{}: {} - {}".format(self.nome, self.carga_horaria, self.teoria)

    class Meta:
        db_table = 'Disciplina'