
from django.db import models
from .Curso import Curso

class ArquivosQuestao(models.Model):
    arquivo = models.CharField(max_length=500)

    class Meta:
        db_table = 'ArquivosQuestao'