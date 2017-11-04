
from django.db import models

class Professor(models.Model):
    ra = models.IntegerField(primary_key=True)
    apelido = models.CharField(max_length=30,unique = True, null = True)
    nome = models.CharField(max_length =  120)
    email = models.CharField(max_length =  80)
    celular = models.CharField(max_length =  11)

    class Meta:
        db_table = 'Professor'