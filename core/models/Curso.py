from django.db import models

class Curso(models.Model):
    sigla = models.CharField(max_length=10)
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome