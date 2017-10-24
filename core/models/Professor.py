from django.db import models

class Usuarios(models.Model):
    ra = 111111
    senha = 'teste123'

class Professor(models.Model):
    curso = models.CharField()
    endereco = 'la em casa'
    idade = 19
    senha = 'teste123'
    cursos = []