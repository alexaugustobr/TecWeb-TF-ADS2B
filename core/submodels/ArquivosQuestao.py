
from django.db import models

class ArquivosQuestao(models.Model):
    questao = models.ForeignKey(to='Questao', related_name="arquivosQuestao", null=False, blank=False) #onetomany
    arquivo = models.CharField(max_length=500)

    class Meta:
        db_table = 'ArquivosQuestao'

from .Questao import Questao
from .Curso import Curso