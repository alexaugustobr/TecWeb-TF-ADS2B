
from django.db import models
from .Curso import Curso
from .Aluno import Aluno
from .Questao import Questao

class Reposta(models.Model):
    aluno = models.ForeignKey(to='Aluno', related_name="respostas", null=False, blank=False) #onetomany
    questao = models.ForeignKey(to='Questao', related_name="respostas", null=False, blank=False) #onetomany
    data_avaliacao = models.DateField()
    nota = models.DecimalField(max_digits=4,decimal_places=2)
    avaliacao = models.TextField()
    descricao = models.TextField()
    data_de_envio = models.TextField()

    class Meta:
        db_table = 'Reposta'