from django.db import models

#TODO candidatura
class Candidato(models.Model):
    nome = models.CharField(max_length =  120, null=True)
    ra = models.CharField(max_length = 80, null=True)
    email = models.CharField(max_length =  80, null=True)
    celular = models.CharField(max_length =  11, null=True)
    codigo_acesso = models.CharField(max_length =  120, null=True)
    foto = models.ForeignKey(to='ArquivosFoto', related_name="candidatos", null=True, blank=True) #onetomany
    
    #via token
    turma = models.ForeignKey(to='Turma', related_name="candidatos", null=True, blank=True) #onetomany
    aluno = models.ForeignKey(to='Aluno', related_name="candidatos", null=True, blank=True) #onetomany

    #nao entra no form
    matricula_aceita = models.BooleanField(default=False)
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.nome, self.email, self.turma)

    class Meta:
        db_table = 'Candidado'

from .ArquivosFoto import ArquivosFoto
from .Candidato import Candidato
from .Aluno import Aluno