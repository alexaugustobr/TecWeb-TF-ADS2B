from django.contrib import admin

# Register your models here.
from core.models import *

admin.site.register(Curso)
admin.site.register(Aluno)
admin.site.register(ArquivosQuestao)
admin.site.register(ArquivosResposta)
admin.site.register(Disciplina)
admin.site.register(DisciplinaOfertada)
admin.site.register(GradeCurricular)
admin.site.register(Periodo)
admin.site.register(Questao)
admin.site.register(Professor)
admin.site.register(Resposta)
admin.site.register(Turma)
admin.site.register(Candidato)
admin.site.register(ArquivosFoto)