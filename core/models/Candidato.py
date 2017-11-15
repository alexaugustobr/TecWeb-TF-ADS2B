from django.db import models

class Candidato(models.Model):
    nome = models.CharField(max_length =  120, null=True)
    ra = models.CharField(max_length = 80, null=True)
    email = models.CharField(max_length =  80, null=True)
    celular = models.CharField(max_length =  11, null=True)
    codigo_acesso = models.CharField(max_length =  120, null=True)
    confirmado = models.BooleanField(default=False)
    turma = models.ForeignKey(to='Turma', related_name="candidatos", null=True, blank=True) #onetomany
    foto = models.ForeignKey(to='ArquivosFoto', related_name="candidatos", null=True, blank=True) #onetomany
    
    def __str__(self):
        return "{} - {}".format(self.nome, self.email)

    class Meta:
        db_table = 'Candidado'

from .ArquivosFoto import ArquivosFoto
from .Candidato import Candidato