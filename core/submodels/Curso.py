from django.db import models

class Curso(models.Model):
    sigla = models.CharField(max_length=5,primary_key=True,null=False)
    nome = models.CharField(max_length=50,unique=True,null=False)

    class Meta:
        db_table = 'Curso'