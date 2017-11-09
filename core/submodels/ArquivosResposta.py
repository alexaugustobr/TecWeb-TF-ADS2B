
from django.db import models
from .Curso import Curso

class ArquivosResposta(models.Model):
    resposta = models.ForeignKey(to='Resposta', related_name="arquivosResposta", null=False, blank=False) #onetomany
    arquivo = models.CharField(max_length=500)

    class Meta:
        db_table = 'ArquivosResposta'

from .Resposta import Resposta