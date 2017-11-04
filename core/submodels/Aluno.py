
from django.db import models
from .Curso import Curso

class Aluno(models.Model):
    curso = models.ForeignKey(Curso, db_column='sigla_curso')
    nome = models.CharField(max_length=120,null=False,primary_key=True)
    email = models.CharField(max_length=80)
    celular = models.CharField(max_length=11)

    class Meta:
        db_table = 'Aluno'