"""lmsimpacta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#metodo alternativo, importando pasta inteira
#from core.views import index 
from professor.views import *
from core.views import *
from professor.views import *
from aluno.views import * 
from aluno.views.candidato import * 


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^handcode/$', handcode),
    url(r'^contato/$', contato),
    url(r'^cursos/$', cursos),
    url(r'^cursos/detalhes/$', detalheCurso),
    url(r'^cursos/banco-dados/$', bancoDados),
    url(r'^noticias/$', noticias),
    url(r'^login/$', login),
    url(r'^esqueci-senha/$', esqueciSenha),
    url(r'^disciplinas/novo/$', disciplinasNovo),
    url(r'^usuarios/novo/$', usuariosNovo),
    url(r'^aluno/$', painelAluno),
    url(r'^matricular/$', matricular),
    url(r'^professor/$', painelProfessor),
    url(r'^detalheCurso/$', detalheCurso),
    url(r'^detalheNoticia/$', detalheNoticia),
    url(r'^professor/turmas/enviar-email/$', enviarEmailTurma),
    url(r'^candidato-matricula/$', candidatoForm),
    url(r'^professor/turmas$', turmas),
    url(r'^professor/turmas/(?P<idTurma>\d+)/$', turma),
    url(r'^professor/matriculas/$', matriculas),
    url(r'^professor/matriculas/confirmar/$', confirmar),
    url(r'^matricular/confirmar/$', confirmarMatricula),
    
]
