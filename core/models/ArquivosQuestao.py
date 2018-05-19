
from django.db import models

class ArquivosQuestao(models.Model):
    questao = models.ForeignKey(on_delete=models.CASCADE, to='Questao', related_name="arquivosQuestao", null=False, blank=False) #onetomany
    arquivo = models.CharField(max_length=500)

    def __str__(self):
        return "{}: {}".format(self.questao, self.id)
    class Meta:
        db_table = 'ArquivosQuestao'

from .Questao import Questao
from .Curso import Curso