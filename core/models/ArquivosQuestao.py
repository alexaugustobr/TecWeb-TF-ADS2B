
from django.db import models

class ArquivosQuestao(models.Model):
    questao = models.ForeignKey(to='Questao', related_name="arquivosQuestao", null=False, blank=False) #onetomany
    arquivo = models.FileField(upload_to="arquivos/")

    def __str__(self):
        return "{}: {}".format(self.questao, self.id)
    class Meta:
        db_table = 'ArquivosQuestao'

from .Questao import Questao
from .Curso import Curso