
from django.db import models
from .Usuario import Usuario
class Professor(Usuario):
    #ra = models.IntegerField(unique = True, null = False)
    apelido = models.CharField(max_length=30,unique = True, null = True)
    #nome = models.CharField(max_length =  120)
    #email = models.CharField(max_length =  80)
    celular = models.CharField(max_length =  11)

    def __str__(self):
        return "{} - {}".format(self.ra, self.apelido)

    class Meta:
        db_table = 'Professor'