from django.contrib.auth.models import AbstractBaseUser, UserManager, BaseUserManager
from django.db import models
from .managers.UsuarioManager import UsuarioManager
ALUNO = 'A'
PROFESSOR = 'P'
COORDENADOR = 'C'
PERFIS = (
     (ALUNO,'Aluno'),
     (PROFESSOR,'Professor'),
     (COORDENADOR,'Coordenador')
)



class Usuario(AbstractBaseUser):
    ra = models.IntegerField("RA", unique=True)
    nome = models.CharField("Nome", max_length=100, blank=True)
    email = models.EmailField("E-Mail", unique=True)
    ativo = models.BooleanField("Ativo", default=True) 
    perfil = models.CharField("Perfil", max_length=1, choices=PERFIS, default='C')
    password = models.CharField(max_length=150)

    USERNAME_FIELD = 'ra'

    objects = UsuarioManager()

    @property
    def is_staff(self):
        return self.perfil == 'C'

    def has_perm(self, perm, obj=None):
	    return True
    def has_module_perms(self, app_label):
	    return True

    def get_short_name(self):
        return self.nome

    def get_full_name(self):
        return self.nome

    def __str__(self):
        return str(self.ra)

    class Meta:
        db_table = 'Usuario'