from django.db import models

class Candidato(models.Model):
    nome = models.CharField(max_length =  120)
    email = models.CharField(max_length =  80)
    celular = models.CharField(max_length =  11)
    codigo_acesso = models.CharField(max_length =  120)
    confirmado = models.BooleanField()
    turma = models.ForeignKey(to='Turma', related_name="candidatos", null=False, blank=False) #onetomany
    foto = models.ForeignKey(to='ArquivosFoto', related_name="candidatos", null=False, blank=False) #onetomany

    def __str__(self):
        return "{} - {}".format(self.nome, self.email)

    class Meta:
        db_table = 'Candidado'

from .ArquivosFoto import ArquivosFoto
from .Candidato import Candidato