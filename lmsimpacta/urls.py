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
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="home"),
    url(r'^handcode/$', handcode),
    url(r'^contato/$', contato),
    url(r'^cursos/$', cursos),
    url(r'^cursos/([A-Z,a-z]+)', detalheCurso),
    url(r'^cursos/banco-dados/$', bancoDados),
    url(r'^noticias/$', noticias),
    #url(r'^login/$', loginHome),
    url(r'^esqueci-senha/$', esqueciSenha),
    url(r'^disciplinas/novo/$', disciplinasNovo),
    url(r'^usuarios/novo/$', usuariosNovo),
    url(r'^aluno/$', painelAluno),
    url(r'^matricular/$', matricular),
    url(r'^professor/$', painelProfessor),
    url(r'^detalheCurso/$', detalheCurso),
    url(r'^detalheNoticia/$', detalheNoticia),
    url(r'^professor/turmas/enviar-email/$', enviarEmailTurma),
    url(r'^professor/turmas$', turmas),
    url(r'^api/professor/turmas$', APIturmas),
    url(r'^professor/turmas/(?P<idTurma>\d+)/$', turma),
    url(r'^professor/matriculas/$', matriculas),
    url(r'^avaliacoes/$', avaliacoes),
    url(r'^avaliacoes/$', boletim),
    url(r'^avaliacoes/(?P<data>\d{4}-\d{2}-\d{2})/$', questaoAberta),
    url(r'^aluno/avaliacoes/responder/$', questaoAbertaResponder),
    url(r'^confirmar-matricula/$', confirmarMatricula),
    url(r'^detalheNoticia2/$', detalheNoticia2),
    url(r'^professor/matriculas/confirmar/$', confirmar),
    url(r'^professor/matriculas/recusar/$', recusar),
    url(r'^professor/exercicios/cadastrar-exercicio/$', questao),
    url(r'^professor/exercicios/$', questoes),
    url(r'^professor/exercicios/turmas/(?P<idTurma>\d+)/recebidos', exerciciosRecebidos),
    url(r'^professor/exercicios/turmas/pendentes', turmasPendentes),
    url(r'^professor/exercicios/turmas/(?P<idTurma>\d+)/pendentes', exerciciosPendentes),
    url(r'^professor/exercicios/avaliar/$', exerciciosRecebidosAvaliar),
    url(r'^professor/exercicios/turmas/$', exercicios),
    url(r'^matricular/confirmar/$', confirmarMatricula),
    url(r"^login/", login, {"template_name":"login/login.html"}), 
    url(r"^logout/", logout, {'next_page': 'home'}),
]

