
from django.db import models
from .Curso import Curso

class ArquivosResposta(models.Model):
    resposta = models.ForeignKey(on_delete=models.CASCADE, to='Resposta', related_name="arquivosResposta", null=False, blank=False) #onetomany
    arquivo = models.CharField(max_length=500)

    def __str__(self):
        return "{}: {}".format(self.resposta, self.id)

    class Meta:
        db_table = 'ArquivosResposta'

from .Resposta import Resposta