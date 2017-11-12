
from django.db import models

class ArquivosFoto(models.Model):
    arquivo = models.CharField(max_length=10000)

    def __str__(self):
        return "{}: {}".format(self.questao, self.id)
    class Meta:
        db_table = 'ArquivosFoto'
