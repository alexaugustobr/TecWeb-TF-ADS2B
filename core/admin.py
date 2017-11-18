from django.contrib import admin


# Register your models here.
from core.models import *

from django.contrib.auth.admin import UserAdmin

from django import forms
class NovoAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('ra','email', 'nome','curso')

    def save(self, commit=True):
        user = super(NovoAlunoForm, self).save(commit=False)
        user.set_password('asdf1234')
        user.perfil = 'A'
        if commit:
            user.save()
        return user

class AlterarAlunoForm(forms.ModelForm):
     class Meta:
         model = Aluno
         fields = ('email', 'nome', 'curso')

class AlunoAdmin(UserAdmin):
    form = AlterarAlunoForm
    add_form = NovoAlunoForm
    list_display = ('email', 'nome', 'curso')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('email', 'nome', 'curso')}),)
    add_fieldsets = ((None, { 'fields': ('ra', 'email', 'nome', 'curso')} ),)
    search_fields = ('ra ',)
    ordering = ('ra',)
    filter_horizontal = ()

admin.site.register(Aluno,AlunoAdmin)
admin.site.register(Usuario) 
admin.site.register(Curso)
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