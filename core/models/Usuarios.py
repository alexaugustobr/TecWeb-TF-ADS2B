from django.contrib.auth.models import AbstractBaseUser, UserManager

ALUNO = 'A'
PROFESSOR = 'P'
COORDENADOR = 'C'
PERFIS = (
     (ALUNO, 'Aluno'),
     (PROFESSOR, 'Professor'),
     (COORDENADOR, 'Coordenador')
)

class UsuarioManager(BaseUserManager):
       use_in_migrations = True

    def _create_user(self, ra, password, **extra_fields):
        if not ra:
            raise ValueError('RA precisa ser preenchido')
        user = self.model(ra=ra, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, ra, password = None, **extra_fields):
        return self._create_user(ra, password, **extra_fields)

    def create_superuser(self, ra, password, **extra_fields):
        return self._create_user(ra, password, **extra_fields)


class Usuario(AbstractBaseUser):
    ra = models.IntegerField("RA", unique = True)
    senha = models.CharField("Senha", max_length = 100)
    nome = models.CharField("Nome", max_length = 100, blank = True)
    email = models.EmailField("E-Mail", unique = True)
    ativo = models.BooleanField("Ativo", default = True)
    perfil = models.CharField("Perfil", max_length = 1, choices = PERFIS)


    USERNAME_FIELD = 'ra'
    REQUIRED_FIELDS = ['nome', 'email']

    object = UsuarioManager

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
        return self. nome